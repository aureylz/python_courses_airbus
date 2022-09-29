---
marp: true
theme: default
style: |
    img[alt~="center"] {
      display: block;
      margin: 0 auto;
    }
---

<!-- author: Yves Campmas -->
<!-- header: Objets with Powershell-->

# Script in Powershell

---

IDE for powershell

---

- Powershell have a dedicated IDE : Powershell ISE

(screenshot)

- Not new features, only security patches
- Replaced by Visual Studio Code
- Installed by default from Windows Server 2012

---

- Intellisense (autocompletion) with CTRL+J
- Syntaxic color
- remote connection available
- Snippet available

---

(screenshot ISE with snippet)

---

- Visual studio code is more advisable IDE
- Don't forget to install Powershell extensions

(screenshot vscode)

---

# Debugging

- Very practical to debug your script
- Put your breakpoint and check step by step

| Keybord | Description |
| --- | --- |
|F5|Start/continue/pause|
|F9|Activate/deactivate breakpoint|
|F10|Step Over|
|F11|Step Into|

Link: https://code.visualstudio.com/docs/editor/debugging

---

# Operators

---

## Comparison Operator

| Operator | Description |
| --- | --- |
|-eq|Equal|
|-ne|Not Equal|
|-gt|Greater than|
|-ge|Greater than or equal to|
|-lt|Less than|
|-le|Less than or equal to|

- Don't confuse with other script languages (==, >, <, etc.)
- Not senstive case by default, you need to add "-c" (example: -ceq)

---

## Comparison in array Operator

| Operator | Description |
| --- | --- |
|-in|Value is in collection|
|-notin|Value is not in collection|
|-contains|collection contains a value|
|-notcontains|collection not contains a value|

example :
    - 'Pierre,'Paul','Jacques' -contains 'Pierre' is true

---

## Logical Operator

| Operator | Description |
| --- | --- |
|-and|AND logical|
|-or|OR logical|
|-not or !|NO Logical |

- Check your expression is true or false

example:
    - ('a' -eq 'a') is true
    - ('a' -eq 'a') -or (8 -eq 9) is true

---

## Divide and combine Operator

| Operator | Description |
| --- | --- |
|-split|split your string into subtring|
|-join|join your multiple string into a single string|

example:
    - "a;b;c;d;e" -split ";" return an array
    a
    b
    c
    d
    e

---

link

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_operators?view=powershell-5.1
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_comparison_operators?view=powershell-5.1
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logical_operators?view=powershell-5.1

---

# Instructions

---

## Loop

- Create a loop that runs command until the condition test is true

````powershell
Foreach ($item in $collection)
{
    # code
}
````

````powershell
For ($i = 1; $i -lt 99; $i++)
{
    # code
}
````

---

````powershell
While (<condition>)
{
    # code
}
````

````powershell
Do
{
    # code
}
While (<condition>)
````

---

- Be careful to avoid an infinite loop !

![w:300 center](./image/dev_loop.jpg)

- No this problem with foreach !

---

Link :
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_foreach?view=powershell-5.1
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_while?view=powershell-5.1

---

Conditional tests

You will orient your code by condition

````powershell
if (<test1>) {
    # if test1 is OK
}
elseif (<test2>) {
    # if test1 is not OK and test2 is OK
}
else {
    <statement list 3>
}
````

---

Interesting if you have many "if"

````powershell
Switch (<test-expression>)
{
    <result1-to-be-matched> {<action>}
    <result2-to-be-matched> {<action>}
}

````

---

Link:
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_if?view=powershell-5.1
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_switch?view=powershell-5.1

---

# Functions and scripts

---

## Functions

- instruction list with a name assign by you
- nice to use many times and avoid the copy/paste
- function have a dedicated task
- the specifications function are :
  - Name
  - Scope (optional)
  - Parameter (optional)
  - code block

---

- Example

````powershell
function [<scope:>]Myfunction
{
    param (
        $param1,
        $param2
    )
  
  $param1 + $param2

  return $value
}
````

- function name : MyFunction (not senstive case)
- parameters : $param1 and $param2
- return : $param1 + $param2

---

- Be careful: your function can return many values
- Function not return only "return", but all display during execution function

````powershell
function test
{
param (
        $param1,
        $param2
    )

  $value = $param1 + $param2
  $param1 + $param2
  return $value
}

PS  >test -param1 2 -param2 3
5
5
````

---

- You can improve your function to "advanced function"
- Easy way to create cmdlets (No compilation .Net)
- Use [CmdletBinding()] in the function (just before param())
- Some example :
  - Possibility to use input processing (pipeline)
  - Whatif, Verbose, ErrorAction, etc. are automaticaly introduce
  - More possibilities for the parameters
  - Many times for the development simplify

---

example :

````powershell
function get-myresult
{
  [CmdletBinding()]
  param (
        [Parameter(Mandatory=$true)]
        [int]$param1,
        [ValidateScript({$_ -gt 5})]
        $param2
    )

  $value = $param1 + $param2

  return $value
}

````

---

link:

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions?view=powershell-5.1
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced?view=powershell-5.1

---

## Script

- Script is a file with instruction list (code, variable, function, etc.)
- Extension for powershell script is "*.ps1"
- You can split your script to many scripts
- Best practice for your script (in order) :
  - Script information (description, author, version, etc.)
  - Parameters (optional)
  - Constante (optional)
  - Functions (optional)
  - main script

---

Execute a script :

- In powershell console, two ways :

& <Path>\myscript.ps1
. <Path>\myscript.ps1

*the second way (".") is DotSourcing. The script will perform with the current scope (if you declare a variable before, the script will know the variable)*

- ISE powershell or Visual Studio Code with F5
- Scheduled tasks in Windows

---

## Execution Policies

Control execution commands for users.

- Restricted : no way to executte ps1 file
- AllSigned : only ps1 signed file are authorized
- RemoteSigned : Block the script from internet
- Unrestricted : All script can be performed (only warning message for internet script)
- ByPass : No restriction

---

# File management

---

- Manage the files in Powershell is very easy
- Cmdlet dedicated to manage item with the noun **item** and **childitem**

| Cmdlet | Description |
| --- | --- |
|Get-Location|Display the current path|
|Set-Location|Move in other path|
|Get-Item|Get the Item|
|New-Item|Create a new item|
|Remove-Item|Remove an item|
|Move-Item|Move an item|
|Copy-Item|Copies an item from one location to another|

---

## Redirection

- You can redirect your result in files

| Cmdlet | Description |
| --- | --- |
|Out-File|Redirect the stream to the file (parameter available)|
|>|Send specified stream to a file|
|>>|Append specified stream to a file|
|>&1|Redirects the specified stream to the Success stream|

- Cmdlet **Content** noun to write in the files

---

- Redirect your different stream with cmdlet **Write** verb

| Cmdlet | Description |
| --- | --- |
|Write-Output|Success Stream|
|Write-Error|Error Stream|
|Write-Warning|Warning Stream|
|Write-Verbose|Verbose Stream|
|Write-Debug|Debug Stream|

---

Link :
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_redirection?view=powershell-5.1

---

- Export your objects to CSV files
- Very interesting to generate reports and store your result

````powershell
Get-Process | Export-Csv -path c:\temp\myprocess.csv -Encoding UTF8 -Delimiter ";" -NoTypeInformation
````

- And the inverse is possible : import CSV to manipulate the data

````powershell
$listobj = Import-Csv -Path "c:\temp\myprocess.csv" -Delimiter ";"
````

---

- Export/import your objects with the cmdlet *-CliXML
- Serialization/Deserialization process
- Remote Powershell use similary process

````powershell
Get-Service | Export-CliXML c:\temp\Services.clixml
````

---

Questions ?

---