# Practica-1-IA
Sistema Experto de Inversiones

📚 Introducción

Este proyecto fue desarrollado como parte del Trabajo Práctico 1 de la materia Introducción a la Inteligencia Artificial de la Universidad Nacional de Colombia.

El objetivo es implementar un sistema híbrido de inteligencia artificial que combine:
	•	Sistemas Expertos basados en reglas (Experta)
	•	Lógica Difusa (Scikit-Fuzzy)
	•	Ontologías y razonamiento semántico (RDFLib y OWL-RL)

El dominio de aplicación elegido es la toma de decisiones de inversión, ayudando a inversionistas a escoger opciones basadas en su perfil, el mercado y la rentabilidad esperada.

⸻

🧠 Componentes

Sistema Experto
	•	Modela reglas lógicas basadas en perfiles de inversionistas, tipos de activos y objetivos financieros.
	•	Gestiona la inferencia mediante hechos y reglas con control de ejecución y prioridades.

Lógica Difusa
	•	Modela la incertidumbre en variables como el riesgo de inversión, la rentabilidad y la volatilidad del mercado.
	•	Utiliza funciones de pertenencia triangulares, trapezoidales y gaussianas.
	•	Implementa reglas difusas con operadores AND, OR y NOT.

Ontología
	•	Representa el conocimiento del dominio financiero usando RDF y RDFS.
	•	Define clases, propiedades y relaciones jerárquicas para activos, inversionistas y objetivos.
	•	Utiliza razonamiento automático para inferir nuevos hechos.

⸻

🔄 Integración
	•	La ontología y la lógica difusa alimentan al sistema experto.
	•	El sistema experto utiliza los resultados para realizar recomendaciones de inversión contextualizadas y más inteligentes.

⸻

🚀 Tecnologías usadas
	•	Python 3
	•	Experta
	•	Scikit-Fuzzy
	•	RDFLib
	•	OWL-RL

⸻

📋 Requisitos
	•	Python 3.8 o superior
	•	Bibliotecas: experta, scikit-fuzzy, rdflib, owlrl

Instalación rápida:
pip install experta scikit-fuzzy rdflib owlrl


⸻

🎯 Ejecución

Cada módulo (experto, difuso, ontologia) es independiente y puede ser ejecutado por separado.
El flujo general integra los resultados de todos los componentes para realizar recomendaciones finales.

⸻

🎥 Sustentación
	•	El proyecto cuenta con un video tipo pitch demostrando la solución implementada.
	•	Enlace al video

⸻

📜 Licencia

Uso académico únicamente.
