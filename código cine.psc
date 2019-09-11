Proceso sin_titulo
	Escribir "Cine"
	Escribir "Clasificación de películas:"
	Escribir "Clasificación A: películas para niños} fantasía, aventura, ciencia ficción"
	Escribir "Clasificación B: películas para jóvenes y adultos} aventura, ciencia ficción, terror."
	Escribir "Clasificación C: películas para adultos} ciencia ficción, terror, romance."
	//procedimiento
	Escribir "¿Qué edad tienes?"
	Leer edad
	si edad < 13
		Escribir "No puedes ver una película clasificación C o clasificación B."
		Escribir "Puedes ver una película clasificación A."
	SiNo
		si edad <18
			Escribir "No puedes ver una película clasificación C."
			Escribir "Puedes ver una película clasificación B o clasificación A."
		SiNo
			si edad > 18
				Escribir "Puedes ver películas clasificación A, B y C."
			FinSi
		FinSi
	FinSi
	
FinProceso
