' todo:
' 1. Implement error handling. Remove Stops.
' 2. Think of more sanity checks to implement.
' 3. Match unaccented vowels to accented but not vica-versa?
' 4. Implement ability to type in pronoun + aux + conjugated verb and display matches
' 5. Implement as-you-type verb matches instead of none or all.
' 6. Go over Notes field in xml file. Some Notes call for an updating/correcting of the conjugations, some cite programming bugs.
' 7. Option to use primary conjugation if alternates are listed [12] or (1|2). In xml file, make xx|yy into (xx|yy)???
' 8. Test against a list of many infinitives. Compare against a website such as la-conjugation.
' 9. Check if db can be compressed (becter and similar). Check all lines against each other. Should only differ by infinitive.(?)

Class MainWindow

    Sub New()

        ' This call is required by the designer.
        InitializeComponent()

        ' Add any initialization after the InitializeComponent() call.
        DataContext = Me
    End Sub

    Public Property ProtoNodeList As Xml.XmlNodeList
    Public Property avoirNode As Xml.XmlNode
    Public Property êtreNode As Xml.XmlNode
    Public Property Regexes As New Dictionary(Of Text.RegularExpressions.Regex, Xml.XmlNode)

    Private Sub MainWindow_Loaded(ByVal sender As Object, ByVal e As System.Windows.RoutedEventArgs) Handles Me.Loaded
        Dim xr As New Xml.XmlDocument
        Dim DataBasePath As String = "..\..\..\verbs-0-2-0.xml"
        Dim ConjugationsPath As String = "..\..\..\conjugations-0-2-0.csv" ' UTF-8, comma delimited
        Try
            xr.Load(DataBasePath)
        Catch ex As Exception
            MsgBox("Unable to load verb database at " & DataBasePath & ". Exception:" & ex.Message)
            Close()
        End Try
        ProtoNodeList = xr.SelectNodes("/Conjugator/Prototype")
        Dim lastRegex As String = ""
        Dim group As String = ""
        Dim DefaultER As Text.RegularExpressions.Regex = Nothing
        Dim DefaultIR As Text.RegularExpressions.Regex = Nothing
        For Each n As Xml.XmlNode In ProtoNodeList
            ' must not have uppercase letter
            For Each a As Xml.XmlAttribute In n.Attributes
                If a.Name <> "NOTES" AndAlso a.Value <> a.Value.ToLower Then Stop
            Next
            ' process REGEX per our needs
            Dim regex As String = n.Attributes("REGEX").Value
            Debug.WriteLine("Original REGEX:" & regex)
            Select Case regex
                Case "avoir"
                    avoirNode = n
                Case "être"
                    êtreNode = n
                Case Else
                    ' do nothing
            End Select
            Dim s As String = ""
            Dim brackets As Integer
            For Each cc As Char In regex
                Select Case cc
                    Case "a", "â"
                        s &= If(brackets, "aâ", "[aâ]")
                    Case "e", "è", "é", "ê"
                        s &= If(brackets, "eèéê", "[eèéê]")
                    Case "h"
                        s &= cc
                    Case "i", "ï", "î"
                        s &= If(brackets, "iïî", "[iïî]")
                    Case "o" ' no variations
                        s &= cc
                    Case "u", "û"
                        s &= If(brackets, "uû", "[uû]")
                    Case "["
                        brackets += 1
                        s &= cc
                    Case "]"
                        brackets -= 1
                        s &= cc
                    Case "'"
                        s &= cc
                    Case ".", "*", "?", "|", "(", ")" ' regex metasymbols
                        s &= cc
                    Case Else
                        If IsVowel(cc) Then Stop
                        s &= cc
                End Select
            Next
            If brackets <> 0 Then Stop
            s = "^(" & s & ")$"
            Debug.WriteLine("PostProcessed REGEX:" & s)
            Dim newRegex As New Text.RegularExpressions.Regex(s)
            ' Sanity checks
            Dim Radical As String = n.Attributes("RADICAL").Value
            'If Radical = "" Then Stop ' être, aller, avoir are ""
            Dim Ending As String = n.Attributes("ENDING").Value
            If Ending = "" Then Stop
            Dim Infinitive As String = n.Attributes("INFINITIVE").Value
            If Infinitive <> (Radical & Ending) Then Stop ' Infinitive must be composed off Radical + Ending
            If Not newRegex.IsMatch(Infinitive) Then Stop ' Infinitive must match this Regex
            ' check regex ordering sanity
            Dim FirstRegex As String = regex.Split("|")(0)
            Select Case FirstRegex
                Case ".*er"
                    If Regexes.Count = 0 Then Stop
                    If lastRegex.First <> "." Then Stop
                    lastRegex = ""
                    DefaultER = newRegex
                Case ".*ir"
                    If Regexes.Count = 0 Then Stop
                    If lastRegex.First <> "." Then Stop
                    lastRegex = ""
                    DefaultIR = newRegex
                Case ".*re"
                    Stop ' todo: can't happen, no such case
                    If Regexes.Count = 0 Then Stop
                    If lastRegex.First <> "." Then Stop
                    lastRegex = ""
                Case Else
                    If FirstRegex.Length < 4 Then Stop
                    If regex <= lastRegex AndAlso Not (FirstRegex.First = "." AndAlso lastRegex.First <> ".") Then
                        ' exceptions to ascending order
                        Select Case regex
                            Case ".*ger"
                            Case ".*dormir"
                            Case ".*voir|.*oir"
                            Case ".*andre|.*endre|.*ondre|.*erdre|.*ordre|.*eurdre"
                            Case Else
                                Stop
                        End Select
                    End If
            End Select
            ' check that all endings in list are identical
            Dim FirstRegexEnding As String = FirstRegex.Substring(FirstRegex.Length - 2, 2)
            For Each ss As String In regex.Split("|")
                If ss.Substring(ss.Length - 2, 2) <> FirstRegex.Substring(FirstRegex.Length - 2, 2) Then Stop
            Next
            If lastRegex = "" Then
                Select Case group
                    Case ""
                        group = "er"
                    Case "er"
                        group = "ir"
                    Case "ir"
                        group = "re"
                    Case "re"
                        Stop
                    Case Else
                        If FirstRegexEnding <> group Then Stop
                End Select
            End If
            For Each r As Text.RegularExpressions.Regex In Regexes.Keys
                ' no previous regex should match this infinitive
                If r.IsMatch(Infinitive) Then Stop
                ' no previous regex should match any of this regex's parts
                For Each ss As String In regex.Split("|")
                    If Not ss.Contains(".") AndAlso r.IsMatch(ss) Then Stop
                Next
            Next
            Regexes.Add(newRegex, n)
            lastRegex = regex
        Next
        If lastRegex.First <> "." Then Stop
        If group <> "re" Then Stop
        If avoirNode Is Nothing OrElse êtreNode Is Nothing Then Stop
        If DefaultER Is Nothing OrElse DefaultIR Is Nothing Then Stop
        DataGrid1.DataContext = ProtoNodeList
        ' create xml file of all model Infinitives
        Dim fidb As New IO.FileInfo(DataBasePath)
        Dim ficp As New IO.FileInfo(ConjugationsPath)
        If True OrElse fidb.LastWriteTimeUtc > ficp.LastWriteTimeUtc Then
#If 1 Then
            ' write all model infinitives to csv file for loading into spreadsheet for inspection
            ' printing using OfficeLibre: A4 paper, landscape, 73% scale, headers off, footers off, top/bottom = .20
            ' printing using OfficeLibre: A4 paper, landscape, 60% scale, headers off, footers off, top/bottom=.90, left/right=.20
            Dim sw As New IO.StreamWriter(ficp.FullName)
            'sw.WriteLine("Conjugation,je,tu,il,nous,vous,ils")
            Dim ModelConjugations As New Collections.ObjectModel.ObservableCollection(Of Tenses)
            For Each kp As KeyValuePair(Of Text.RegularExpressions.Regex, Xml.XmlNode) In Regexes
                Dim infinitive As String = kp.Value.Attributes("INFINITIVE").Value
                Try
                    sw.WriteLine()
                    MakeConjugations(Conjugations, kp.Key, infinitive, kp.Value)
#If 0 Then ' want model conjugations?
                    Select Case infinitive.Substring(infinitive.Length - 2, 2)
                        Case "er"
                            MakeConjugations(ModelConjugations, DefaultER, infinitive, Regexes(DefaultER))
                        Case "ir", "ïr"
                            MakeConjugations(ModelConjugations, DefaultIR, infinitive, Regexes(DefaultIR))
                        Case "re"
                            ' todo: how to show irregular -re endings?
                        Case Else
                            Stop
                    End Select
#End If
                    For i As Integer = 0 To Conjugations.Count - 1
                        sw.WriteLine(infinitive & " " & Conjugations(i).Conjugation & "," & ShowIrregulars(Conjugations(i), If(ModelConjugations.Count = 0, Nothing, ModelConjugations(i))))
                    Next
                    Conjugations.Clear()
                    ModelConjugations.Clear()
                Catch ex As Exception
                    Stop
                End Try
            Next
            sw.Close()
#Else
                    ' incomplete - write all model infinitives to xml file
                    Dim xs As New Xml.XmlWriterSettings
                    xs.Indent = True
                    Dim xw As Xml.XmlWriter = Xml.XmlWriter.Create(ficp.FullName, xs)
                    xw.WriteStartElement("Infinitives")
                    For Each kp As KeyValuePair(Of Text.RegularExpressions.Regex, Xml.XmlNode) In Regexes
                        MakeConjugations(kp.Key, kp.Value.Attributes("INFINITIVE").Value, kp.Value)
                        xw.WriteStartElement("Infinitive")
                        For Each t As Tenses In Conjugations
                            Try
                                xw.WriteElementString(t.Conjugation.Replace(" ", "-"), t.je & "," & t.tu & "," & t.il & "," & t.nous & "," & t.vous & "," & t.ils)
                            Catch ex As Exception
                                Stop
                            End Try
                        Next
                        xw.WriteEndElement() ' Infinitive
                        Conjugations.Clear()
                    Next
                    xw.WriteEndElement() ' Infinitives
                    xw.Close()
#End If
        End If
        UpdateChanges(sender, e)
    End Sub

    Private Function ShowIrregulars(ByVal Tenses As Tenses, ByVal ModelTenses As Tenses) As String
        ShowIrregulars = Tenses.je
        If ModelTenses IsNot Nothing AndAlso Tenses.je <> ModelTenses.je Then ShowIrregulars &= "<" & ModelTenses.je.Split(" ").Last & ">"
        ShowIrregulars &= "," & Tenses.tu
        If ModelTenses IsNot Nothing AndAlso Tenses.tu <> ModelTenses.tu Then ShowIrregulars &= "<" & ModelTenses.tu.Split(" ").Last & ">"
        ShowIrregulars &= "," & Tenses.il
        If ModelTenses IsNot Nothing AndAlso Tenses.il <> ModelTenses.il Then ShowIrregulars &= "<" & ModelTenses.il.Split(" ").Last & ">"
        ShowIrregulars &= "," & Tenses.nous
        If ModelTenses IsNot Nothing AndAlso Tenses.nous <> ModelTenses.nous Then ShowIrregulars &= "<" & ModelTenses.nous.Split(" ").Last & ">"
        ShowIrregulars &= "," & Tenses.vous
        If ModelTenses IsNot Nothing AndAlso Tenses.vous <> ModelTenses.vous Then ShowIrregulars &= "<" & ModelTenses.vous.Split(" ").Last & ">"
        ShowIrregulars &= "," & Tenses.ils
        If ModelTenses IsNot Nothing AndAlso Tenses.ils <> ModelTenses.ils Then ShowIrregulars &= "<" & ModelTenses.ils.Split(" ").Last & ">"
    End Function

    Private Function IsVowel(ByVal s As String) As Boolean
        Dim c As Char = s.First
        IsVowel = Char.IsLetter(c) AndAlso (Not "bcdfghjklmnpqrstvwxyz".Contains(c) OrElse (c = "h" AndAlso (s.Length = 1 OrElse s(1) <> "a"))) ' if h is silent, use j'
    End Function

    Private Sub MakeConjugations(ByVal Conjugations As Collections.ObjectModel.ObservableCollection(Of Tenses), Regex As Text.RegularExpressions.Regex, ByVal Infinitive As String, ByVal n As Xml.XmlNode)
        For Each c As Control In ConjugationsSP.Children
            If TypeOf c Is CheckBox Then
                Dim cb As CheckBox = DirectCast(c, CheckBox)
                If cb.IsChecked Then
                    Dim match As Text.RegularExpressions.Match = Regex.Match(Infinitive)
                    Dim ending As String = n.Attributes("ENDING").Value
                    Dim radical As String = Infinitive.Substring(0, Infinitive.Length - ending.Length)
                    Dim auxNode As Xml.XmlNode = Nothing
                    Select Case n.Attributes("AUX").Value
                        Case "avoir"
                            auxNode = avoirNode
                        Case "être"
                            auxNode = êtreNode
                        Case Else
                            Stop
                    End Select
                    Conjugations.Add(ConjugateTense(cb.Content, n, radical, auxNode, If(match.Groups.Count = 3, match.Groups(2).Captures(0).Value, "")))
                End If
            End If
        Next
    End Sub

    Public Property Conjugations As New Collections.ObjectModel.ObservableCollection(Of Tenses)
    Public Class Tenses
        Public Property Conjugation As String
        Public Property je As String
        Public Property tu As String
        Public Property il As String
        Public Property nous As String
        Public Property vous As String
        Public Property ils As String
    End Class

    Private Sub InfinitiveTBX_TextChanged(ByVal sender As Object, ByVal e As System.Windows.Controls.TextChangedEventArgs) Handles InfinitiveTBX.TextChanged
        InfinitiveTBX.Text = InfinitiveTBX.Text.ToLower
        UpdateChanges(sender, e)
    End Sub

    Private Sub UpdateChanges(ByVal sender As Object, ByVal e As System.EventArgs)
        DataGrid2.ItemsSource = Nothing
        Conjugations.Clear()
        Dim AllCandidateMatches As New Dictionary(Of Text.RegularExpressions.Regex, Xml.XmlNode)
        For Each kp As KeyValuePair(Of Text.RegularExpressions.Regex, Xml.XmlNode) In Regexes
            If InfinitiveTBX.Text.Length = 0 OrElse kp.Key.IsMatch(InfinitiveTBX.Text) Then AllCandidateMatches.Add(kp.Key, kp.Value)
        Next
        DataGrid1.DataContext = AllCandidateMatches.Values
        If InfinitiveTBX.Text.Length > 3 Then ' minimum length of a French verb
            If AllCandidateMatches.Count > 0 Then
                Dim TopCandidateNode As Xml.XmlNode = AllCandidateMatches.Values(0)
                Dim TopCandidateRegex As Text.RegularExpressions.Regex = AllCandidateMatches.Keys(0)
                MakeConjugations(Conjugations, AllCandidateMatches.Keys(0), InfinitiveTBX.Text, AllCandidateMatches.Values(0))
                DataGrid2.ItemsSource = Conjugations
                For Each c As Control In TensesSP.Children
                    If TypeOf c Is CheckBox Then
                        Dim cb As CheckBox = DirectCast(c, CheckBox)
                        DataGrid2.Columns(c.Tag + 1).Header = cb.Content
                        DataGrid2.Columns(c.Tag + 1).Visibility = If(cb.IsChecked, Visibility.Visible, Visibility.Hidden)
                    End If
                Next
            End If
        End If
    End Sub

    Private Sub ConjugateTenseSimple(ByVal Tenses As Tenses, ByVal Radical As String, ByVal TenseParts As String, Optional ByVal Artical As String = "")
        Dim SplitTenseParts() As String = TenseParts.Split(",".ToCharArray)
        If SplitTenseParts.Length < 6 Then SplitTenseParts = {SplitTenseParts(0), SplitTenseParts(0), SplitTenseParts(0), SplitTenseParts(0), SplitTenseParts(0), SplitTenseParts(0)}
        Dim Articals() As String = Artical.Split(",")
        If Articals.Length < 6 Then Articals = {"", "", "", "", "", ""}
        If SplitTenseParts(0) <> "" Then Tenses.je = Articals(0) & If(IsVowel(Radical & SplitTenseParts(0)), "j'", "je ") & Radical & SplitTenseParts(0).Replace("|", "|" & Radical)
        If SplitTenseParts(1) <> "" Then Tenses.tu = Articals(1) & "tu " & Radical & SplitTenseParts(1).Replace("|", "|" & Radical)
        If SplitTenseParts(2) <> "" Then Tenses.il = Articals(2) & "il " & Radical & SplitTenseParts(2).Replace("|", "|" & Radical) ' il/elle
        If SplitTenseParts(3) <> "" Then Tenses.nous = Articals(3) & "nous " & Radical & SplitTenseParts(3).Replace("|", "|" & Radical)
        If SplitTenseParts(4) <> "" Then Tenses.vous = Articals(4) & "vous " & Radical & SplitTenseParts(4).Replace("|", "|" & Radical)
        If SplitTenseParts(5) <> "" Then Tenses.ils = Articals(5) & "ils " & Radical & SplitTenseParts(5).Replace("|", "|" & Radical)
    End Sub

    Private Sub ConjugateTensePastParticiple(ByVal Tenses As Tenses, ByVal AuxParts As String, ByVal Radical As String, ByVal SplitTenseParts() As String, Optional ByVal Artical As String = "")
        Dim SplitAuxParts() As String = AuxParts.Split(",".ToCharArray)
        Dim Articals() As String = Artical.Split(",")
        If Articals.Length < 6 Then Articals = {"", "", "", "", "", ""}
        If SplitTenseParts(0) <> "" Then Tenses.je = Articals(0) & If(IsVowel(SplitAuxParts(0)), "j'", "je ") & SplitAuxParts(0) & " " & Radical & SplitTenseParts(0).Replace("|", "|" & Radical)
        If SplitTenseParts(1) <> "" Then Tenses.tu = Articals(1) & "tu " & SplitAuxParts(1) & " " & Radical & SplitTenseParts(1).Replace("|", "|" & Radical)
        If SplitTenseParts(2) <> "" Then Tenses.il = Articals(2) & "il " & SplitAuxParts(2) & " " & Radical & SplitTenseParts(2).Replace("|", "|" & Radical) ' il/elle
        If SplitTenseParts(3) <> "" Then Tenses.nous = Articals(3) & "nous " & SplitAuxParts(3) & " " & Radical & SplitTenseParts(3).Replace("|", "|" & Radical)
        If SplitTenseParts(4) <> "" Then Tenses.vous = Articals(4) & "vous " & SplitAuxParts(4) & " " & Radical & SplitTenseParts(4).Replace("|", "|" & Radical)
        If SplitTenseParts(5) <> "" Then Tenses.ils = Articals(5) & "ils " & SplitAuxParts(5) & " " & Radical & SplitTenseParts(5).Replace("|", "|" & Radical)
    End Sub

    Private Function ConjugateTense(ByVal tense As String, ByVal xmltense As Xml.XmlNode, ByVal Radical As String, ByVal auxNode As Xml.XmlNode, ByVal Substitution As String) As Tenses
        ConjugateTense = New Tenses
        ConjugateTense.Conjugation = tense
        Dim ques As String = "que ,que ,qu',que ,que ,qu'"
        Dim PPASSÉ() As String = xmltense.Attributes("PPASSÉ").Value.Replace("?", Substitution).Split(",")
        Dim SplitTenseParts() As String
        If auxNode Is avoirNode Then
            SplitTenseParts = {PPASSÉ(0), PPASSÉ(0), PPASSÉ(0), PPASSÉ(0), PPASSÉ(0), PPASSÉ(0)} ' avoir
        Else
            SplitTenseParts = {PPASSÉ(0), PPASSÉ(0), PPASSÉ(0), PPASSÉ(2), PPASSÉ(2), PPASSÉ(2)} ' etre
        End If
        Select Case tense
            Case "Présent"
                ConjugateTenseSimple(ConjugateTense, Radical, xmltense.Attributes("PRÉSENT").Value.Replace("?", Substitution))
            Case "Passé Composé"
                ConjugateTensePastParticiple(ConjugateTense, auxNode.Attributes("PRÉSENT").Value.Replace("?", Substitution), Radical, SplitTenseParts)
            Case "Imparfait"
                ConjugateTenseSimple(ConjugateTense, Radical, xmltense.Attributes("IMPARFAIT").Value.Replace("?", Substitution))
            Case "Plus-que-parfait"
                ConjugateTensePastParticiple(ConjugateTense, auxNode.Attributes("IMPARFAIT").Value.Replace("?", Substitution), Radical, SplitTenseParts)
            Case "Futur Simple"
                ConjugateTenseSimple(ConjugateTense, Radical, xmltense.Attributes("FUTUR").Value.Replace("?", Substitution))
            Case "Futur Antérieur"
                ConjugateTensePastParticiple(ConjugateTense, auxNode.Attributes("FUTUR").Value.Replace("?", Substitution), Radical, SplitTenseParts)
            Case "Conditionnel Présent"
                ConjugateTenseSimple(ConjugateTense, Radical, xmltense.Attributes("CONDITION").Value.Replace("?", Substitution))
            Case "Conditionnel Passé"
                ConjugateTensePastParticiple(ConjugateTense, auxNode.Attributes("CONDITION").Value.Replace("?", Substitution), Radical, SplitTenseParts)
            Case "Subjonctif Présent"
                ConjugateTenseSimple(ConjugateTense, Radical, xmltense.Attributes("SPRÉSENT").Value.Replace("?", Substitution), ques)
            Case "Subjonctif Passé"
                ConjugateTensePastParticiple(ConjugateTense, auxNode.Attributes("SPRÉSENT").Value.Replace("?", Substitution), Radical, SplitTenseParts, ques)
            Case "Subjonctif Imparfait"
                ConjugateTenseSimple(ConjugateTense, Radical, xmltense.Attributes("SIMPARFAIT").Value.Replace("?", Substitution), ques)
            Case "Subjonctif Plus-que-parfait"
                ConjugateTensePastParticiple(ConjugateTense, auxNode.Attributes("SIMPARFAIT").Value.Replace("?", Substitution), Radical, SplitTenseParts, ques)
            Case "Passé simple"
                ConjugateTenseSimple(ConjugateTense, Radical, xmltense.Attributes("PASSÉ").Value.Replace("?", Substitution))
            Case "Passé Antérieur"
                ConjugateTensePastParticiple(ConjugateTense, auxNode.Attributes("PASSÉ").Value.Replace("?", Substitution), Radical, SplitTenseParts)
            Case "Impératif Présent"
                ConjugateTenseSimple(ConjugateTense, Radical, xmltense.Attributes("IMPÉRATIF").Value.Replace("?", Substitution))
            Case "Infinitif Présent"
                ConjugateTenseSimple(ConjugateTense, Radical, xmltense.Attributes("ENDING").Value.Replace("?", Substitution))
            Case "Participe Présent"
                ConjugateTenseSimple(ConjugateTense, Radical, xmltense.Attributes("PPRESENT").Value.Replace("?", Substitution))
            Case "Participe Passé"
                ConjugateTenseSimple(ConjugateTense, Radical, xmltense.Attributes("PPASSÉ").Value.Replace("?", Substitution))
            Case Else
                Stop
        End Select
    End Function

    Private Sub CloseBtn_Click(ByVal sender As Object, ByVal e As System.Windows.RoutedEventArgs) Handles CloseBtn.Click
        Close()
    End Sub

    Private Sub CheckBox_Click(ByVal sender As System.Object, ByVal e As System.Windows.RoutedEventArgs)
        UpdateChanges(sender, e)
    End Sub

    Private Sub SelectAllConjugationsBtn_Click(ByVal sender As System.Object, ByVal e As System.Windows.RoutedEventArgs)
        For Each c As Control In ConjugationsSP.Children
            If TypeOf c Is CheckBox Then
                Dim cb As CheckBox = DirectCast(c, CheckBox)
                cb.IsChecked = True
            End If
        Next
        UpdateChanges(sender, e)
    End Sub

    Private Sub SelectAllTensesBtn_Click(ByVal sender As System.Object, ByVal e As System.Windows.RoutedEventArgs)
        For Each c As Control In TensesSP.Children
            If TypeOf c Is CheckBox Then
                Dim cb As CheckBox = DirectCast(c, CheckBox)
                cb.IsChecked = True
            End If
        Next
        UpdateChanges(sender, e)
    End Sub

End Class
