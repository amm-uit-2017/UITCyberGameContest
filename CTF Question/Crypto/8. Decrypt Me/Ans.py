Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: D:\Localnew\RE\7 Decrypt If u Can\decrypt.py ===========
>>> """S2V5ID1bMzUsIDQxLCAzNiwgMzQsIDYyLCAxLCAzMiwgMzgsIDU1LCA2MCwgNTMsIDQ5LCAyNiwg\nNDAsIDMyLCAyNiwgNDQsIDM1LCAyNiwgNjAsIDQyLCA0OCwgMjYsMzgsIDM2LDQzLCA1Nl0=\n""".decode("base64")
'Key =[35, 41, 36, 34, 62, 1, 32, 38, 55, 60, 53, 49, 26, 40, 32, 26, 44, 35, 26, 60, 42, 48, 26,38, 36,43, 56]'
>>> st = ""
>>> key = [35, 41, 36, 34, 62, 1, 32, 38, 55, 60, 53, 49, 26, 40, 32, 26, 44, 35, 26, 60, 42, 48, 26,38, 36,43, 56]
>>> for i in key:
	st+=chr(i)

	
>>> st
'#)$">\x01 &7<51\x1a( \x1a,#\x1a<*0\x1a&$+8'
>>> s = '#)$">\x01 &7<51\x1a( \x1a,#\x1a<*0\x1a&$+8'
>>> decrypt(s)
'flag{Decrypt_me_if_you_can}'
>>> 
