import pytz



YESORNOT_CHOICES = (
				('',''),
				('Sim','Sim'),
				('Nao','Não'),
			)

GENDER_CHOICES = (
				('',''),
				('Masculino','Masculino'),
				('Feminino', 'Feminino'),
				('Outros', 'Outros'),
			)

EDUCATION_CHOICES = (
				('',''),
				('Fundamental incompleto','Fundamental incompleto'),
				('Fundamental completo', 'Fundamental completo'),
				('Medio incompleto','Médio incompleto'),
				('Medio completo','Médio completo'),
				('Tecnico incompleto','Técnico incompleto'),
				('Tecnico completo', 'Técnico completo'),
				('Superior incompleto','Superior incompleto'),
				('Superior completo','Superior completo'),
				('Pos-Graduacao', 'Pós-Graduação'),
				('Mestrado', 'Mestrado'),
				('Doutorado', 'Doutorado'),	
				('PHD', 'PHD')					
			)

EDUCATION_CHOICES_FORMATION = (
				('',''),
				('Medio Tecnico','Médio Técnico'),
				('Superior','Superior'),
				('Especializacao','Especialização'),
				('Pos-Graduacao', 'Pós-Graduação'),
				('Mestrado', 'Mestrado'),
				('Doutorado', 'Doutorado'),	
				('PHD', 'PHD')					
			)

LEVEL = (
				('',''),
				('Basico', 'Básico'), 
				('Intermediario', 'Intermediário'),
				('Avancado', 'Avançado'), 
				('Fluente', 'Fluente'),			
			)

HABILITACAO = (
				('',''),
				('A', 'A'), 
				('AB', 'AB'),
				('AC', 'AC'), 
				('AD', 'AD'),	
				('B', 'B'),
				('C', 'C'), 
				('D', 'D'),		
				('E', 'E'),	
			)
USER_TYPE = (
				('Candidato', 'Candidato'), 
				('Empregador', 'Empregador'),
			)

COURSE_TYPE = (
				('',''),
				('Curso de Qualificacao', 'Curso de Qualificação'), 
				('Curso Profissionalizante', 'Curso Profissionalizante'),
				('Palestra', 'Palestra'),
				('Simposio', 'Simpósio'),
			)

BRANCH_ACTIVITY = (
				('',''),
				('Industria', 'Indústria'), 
				('Comercio', 'Comércio'),
				('Prestacao de Servicos', 'Prestação de Serviços'),
				('Outros', 'Outros'),
			)

BRANCH_TYPE = (
				('',''),
				('MEI', 'MEI - Faturamento até R$ 81 mil'), 
				('ME', 'ME - Faturamento até R$ 360 mil'),
				('EPP', 'EPP - Faturamento até R$ 3,6 milhões'),
				('Empresa Normal', 'Empresa Normal - Faturamento superior a R$ 3,6 milhões'),
			)

BRANCH_TYPE = (
				('',''),
				('MEI', 'MEI - Faturamento até R$ 81 mil'), 
				('ME', 'ME - Faturamento até R$ 360 mil'),
				('EPP', 'EPP - Faturamento até R$ 3,6 milhões'),
				('Empresa Normal', 'Empresa Normal - Faturamento superior a R$ 3,6 milhões'),
			)


MARITAL_STATUS = (
				('',''),
				('Solteiro', 'Solteiro(a)'), 
				('Casado', 'Casado(a)'),
				('Divorciado', 'Divorciado(a)'),
				('Outros', 'Outros'),
			)