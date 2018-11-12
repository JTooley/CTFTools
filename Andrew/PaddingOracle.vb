Imports System.Net.Sockets

Module Module1

    Sub Main()
        Dim cipher_String = "xxxxxxx put encoded data here xxxxxxxxxxxxxxxxxxxxxxxxxxxx"

        Dim TelnetClient As New TcpClient
        TelnetClient.Connect("put ip address here", put port here)

        'Wait for password prompt - then send password
        receiveString(TelnetClient)
        sendString(TelnetClient, "put password here")

        Dim message_result As String = ""
        Dim progress = 0
        For block = 1 To 2
            Dim current_block = cipher_String.Substring(32 * block, 32)
            Dim previous_block = cipher_String.Substring(32 * (block - 1), 32)

            Dim intermediate As New List(Of Integer)
            Dim block_result = ""
            For i = 0 To 15
                'So we want to form a string that looks like
                '00000000000000THHHHHREALREALREALREAL
                '0's are our random code which should look like encoded padding values
                'T is our test value which we will try 0 to 255 for
                'H is the values we have already hacked with encoded versions of the padding inserted
                'REAL is the next actual block of cypher text
                Dim known_cypher_byte_hex = previous_block.Substring((16 - i - 1) * 2, 2)
                Dim known_cypher_byte = Convert.ToInt32(known_cypher_byte_hex, 16)

                Dim start_str = ""
                For t = 0 To 14 - i
                    start_str += "00"
                Next

                Dim mid_str As String = ""
                Dim current_padding_byte = i + 1
                For Each t In intermediate
                    mid_str &= (current_padding_byte Xor t).ToString("X2")
                Next

                Dim test_value As Integer = 0
                While (True)
                    Dim test As String = start_str & test_value.ToString("X2") & mid_str & current_block

                    'Send test string and wait for result to return
                    sendString(TelnetClient, test)
                    Dim serverResult = receiveString(TelnetClient)

                    'Check if its the one and doesnt give invalid padding error back
                    If (Not serverResult.Contains("padding")) Then
                        Exit While
                    End If

                    test_value += 1
                    If (test_value > 255) Then
                        Throw New Exception("FAILED !!!! Find is TOO BIG")
                    End If
                End While

                'As we know what padding byte there must be in the plain text and we know what 
                'cypher byte we put in we can deduce the intermediate byte
                Dim intermediate_byte = current_padding_byte Xor test_value

                'This next line decodes what plaintext value intermediate value came from
                Dim hacked_val = intermediate_byte Xor known_cypher_byte

                intermediate.Insert(0, intermediate_byte)
                block_result = Chr(hacked_val) & block_result
                progress += 1
                Console.WriteLine("Progress " & Math.Round(progress * 100 / 32) & "%")
            Next
            message_result &= block_result
        Next

        MsgBox(message_result)
    End Sub

    Sub sendString(TelnetClient As TcpClient, msg As String)
        Dim byt_to_send() As Byte = System.Text.Encoding.ASCII.GetBytes(msg & vbNewLine)
        TelnetClient.Client.Send(byt_to_send, 0, byt_to_send.Length, SocketFlags.None)
    End Sub


    Function receiveString(TelnetClient As TcpClient) As String
        While (TelnetClient.Available = 0)
            System.Threading.Thread.Sleep(10)
        End While

        Dim tmp_recieve(TelnetClient.Available - 1) As Byte
        TelnetClient.Client.Receive(tmp_recieve, 0, tmp_recieve.Length, SocketFlags.None)
        Return System.Text.Encoding.ASCII.GetString(tmp_recieve)
    End Function

End Module
