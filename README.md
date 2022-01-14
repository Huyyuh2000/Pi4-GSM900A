# Project
## Discription
- Raspberry Pi 4 communicate with Module sim gsm 900A via usb port using usb-ttl
- Because of project purpose, we only use sms mode
## Note
### Pyserial Python
- pyserial transfer data in binary so we need to encode string into "utf-8" format when write data and decode "utf-8" format when read
- pyserial using one buffer for read and write to transfer so it may cause conflic when read after write. To avoid this, we need to delay amount of time after write for get full response from gsm. Then we need to handle sended byte in the buffer to get true response
### GSM sms format
#### GSM command
1. Handshake: "AT\r\n"
2. SMS:
- SMS mode: "AT+CMGF=1\r\n"
- Config phone number: "AT+CMGS=\"+84xxxxxxxx\"\r\n" (replace x with your phone number)
- Send text: "Text"
- End text - Send Ctrl+Z in python: char(26)
3. SMS response message:
- "\r\nMESSAGE\r\n"