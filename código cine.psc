Proceso sin_titulo
	Escribir "Cine"
	Escribir "Clasificaci�n de pel�culas:"
	Escribir "Clasificaci�n A: pel�culas para ni�os} fantas�a, aventura, ciencia ficci�n"
	Escribir "Clasificaci�n B: pel�culas para j�venes y adultos} aventura, ciencia ficci�n, terror."
	Escribir "Clasificaci�n C: pel�culas para adultos} ciencia ficci�n, terror, romance."
	//procedimiento
	Escribir "�Qu� edad tienes?"
	Leer edad
	si edad < 13
		Escribir "No puedes ver una pel�cula clasificaci�n C o clasificaci�n B."
		Escribir "Puedes ver una pel�cula clasificaci�n A."
	SiNo
		si edad <18
			Escribir "No puedes ver una pel�cula clasificaci�n C."
			Escribir "Puedes ver una pel�cula clasificaci�n B o clasificaci�n A."
		SiNo
			si edad > 18
				Escribir "Puedes ver pel�culas clasificaci�n A, B y C."
			FinSi
		FinSi
	FinSi
	
FinProceso
