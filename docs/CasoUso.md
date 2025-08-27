## Casos de Uso - TurnoPlus

### **Actores del Sistema**

1. **Cliente/Usuario Final** - Persona que desea reservar un turno
2. **Profesional/Empleado** - Persona que brinda servicios y atiende clientes
3. **Administrador de Negocio** - Propietario o gerente del negocio
4. **Administrador del Sistema** - Super administrador de la plataforma
5. **Sistema de Notificaciones** - Actor automático para envío de emails/SMS
6. **Google Calendar API** - Sistema externo para sincronización

---

## **1. Casos de Uso - Cliente/Usuario Final**

### CU-001: Buscar Negocio y Servicios
**Actor Principal:** Cliente  
**Precondiciones:** Ninguna  
**Postcondiciones:** Cliente encuentra información del negocio y servicios disponibles

**Flujo Principal:**
1. Cliente accede a la URL pública del negocio `/book/:businessSlug`
2. Sistema muestra información del negocio (nombre, dirección, horarios)
3. Sistema lista servicios disponibles con duración y precio
4. Cliente selecciona el servicio deseado
5. Sistema muestra descripción detallada del servicio

**Flujos Alternativos:**
- 2a. Negocio no existe o está inactivo
  - Sistema muestra mensaje de error "Negocio no encontrado"
- 3a. No hay servicios activos disponibles
  - Sistema muestra mensaje "No hay servicios disponibles actualmente"

---

### CU-002: Consultar Disponibilidad
**Actor Principal:** Cliente  
**Precondiciones:** Cliente ha seleccionado un servicio  
**Postcondiciones:** Cliente visualiza horarios disponibles

**Flujo Principal:**
1. Cliente selecciona fecha deseada en calendario
2. Sistema consulta horarios de trabajo del negocio
3. Sistema consulta excepciones de horarios (feriados, vacaciones)
4. Sistema consulta turnos ya reservados
5. Sistema calcula slots disponibles considerando duración del servicio
6. Sistema muestra slots disponibles en formato de grilla horaria
7. Cliente selecciona horario específico

**Flujos Alternativos:**
- 1a. Cliente selecciona fecha pasada
  - Sistema no permite selección y muestra mensaje informativo
- 6a. No hay slots disponibles para la fecha
  - Sistema sugiere fechas alternativas cercanas
- 6b. Negocio cerrado en fecha seleccionada
  - Sistema muestra mensaje con horarios de apertura

---

### CU-003: Reservar Turno
**Actor Principal:** Cliente  
**Precondiciones:** Cliente ha seleccionado servicio y horario  
**Postcondiciones:** Turno creado en estado "pendiente"

**Flujo Principal:**
1. Sistema solicita datos del cliente (nombre, apellido, email, teléfono)
2. Cliente completa formulario de reserva
3. Cliente opcionalmente agrega notas/comentarios
4. Sistema valida datos ingresados
5. Sistema verifica disponibilidad del slot seleccionado
6. Sistema crea turno en estado "pendiente"
7. Sistema genera token único de confirmación
8. Sistema envía email de confirmación al cliente
9. Sistema muestra página de éxito con instrucciones

**Flujos Alternativos:**
- 4a. Datos inválidos o incompletos
  - Sistema muestra errores de validación específicos
- 5a. Slot ya no disponible (reservado por otro cliente)
  - Sistema informa conflicto y sugiere horarios alternativos
- 8a. Error al enviar email
  - Sistema registra el turno pero notifica problema de email

---

### CU-004: Confirmar Turno
**Actor Principal:** Cliente  
**Precondiciones:** Cliente recibió email de confirmación  
**Postcondiciones:** Turno cambia a estado "confirmado"

**Flujo Principal:**
1. Cliente hace clic en link de confirmación del email
2. Sistema valida token de confirmación
3. Sistema actualiza estado del turno a "confirmado"
4. Sistema registra fecha/hora de confirmación
5. Sistema envía notificación al negocio
6. Sistema muestra página de confirmación exitosa
7. Opcionalmente, sistema crea evento en Google Calendar

**Flujos Alternativos:**
- 2a. Token inválido o expirado
  - Sistema muestra error y opción de contactar al negocio
- 2b. Turno ya confirmado previamente
  - Sistema muestra mensaje informativo

---

### CU-005: Cancelar Turno
**Actor Principal:** Cliente  
**Precondiciones:** Cliente tiene turno reservado  
**Postcondiciones:** Turno cambia a estado "cancelado"

**Flujo Principal:**
1. Cliente hace clic en link de cancelación del email
2. Sistema valida token de cancelación
3. Sistema solicita confirmación de cancelación
4. Cliente confirma cancelación
5. Sistema actualiza estado del turno a "cancelado"
6. Sistema libera slot horario para otros clientes
7. Sistema envía notificación al negocio
8. Sistema muestra confirmación de cancelación

**Flujos Alternativos:**
- 2a. Token inválido
  - Sistema muestra error y datos de contacto del negocio
- 4a. Cliente cancela la operación
  - Sistema no realiza cambios y muestra turno actual

---

## **2. Casos de Uso - Profesional/Empleado**

### CU-006: Iniciar Sesión
**Actor Principal:** Profesional  
**Precondiciones:** Usuario registrado en el sistema  
**Postcondiciones:** Usuario autenticado con acceso al dashboard

**Flujo Principal:**
1. Profesional accede a página de login
2. Profesional ingresa email y contraseña
3. Sistema valida credenciales
4. Sistema genera token JWT
5. Sistema redirige a dashboard principal
6. Sistema registra último acceso

**Flujos Alternativos:**
- 3a. Credenciales incorrectas
  - Sistema muestra error y permite reintentar
- 3b. Cuenta no verificada
  - Sistema solicita verificación de email
- 3c. Cuenta inactiva
  - Sistema muestra mensaje de contacto a soporte

---

### CU-007: Gestionar Agenda Diaria
**Actor Principal:** Profesional  
**Precondiciones:** Usuario autenticado  
**Postcondiciones:** Profesional visualiza y gestiona agenda del día

**Flujo Principal:**
1. Profesional accede a vista de calendario diario
2. Sistema muestra turnos del día actual ordenados cronológicamente
3. Sistema indica estado de cada turno (confirmado, pendiente, etc.)
4. Profesional puede ver detalles de cada turno
5. Profesional puede marcar turnos como completados
6. Profesional puede agregar notas post-atención

**Flujos Alternativos:**
- 2a. No hay turnos para el día
  - Sistema muestra mensaje informativo
- 5a. Turno marcado como "no show"
  - Sistema registra ausencia del cliente

---

### CU-008: Crear Turno Manualmente
**Actor Principal:** Profesional  
**Precondiciones:** Usuario autenticado con permisos de negocio  
**Postcondiciones:** Nuevo turno creado manualmente

**Flujo Principal:**
1. Profesional accede a formulario de nuevo turno
2. Profesional selecciona cliente existente o crea nuevo
3. Profesional selecciona servicio
4. Profesional selecciona fecha y hora
5. Sistema valida disponibilidad
6. Profesional agrega notas si es necesario
7. Sistema crea turno en estado "confirmado"
8. Sistema envía notificación al cliente (opcional)

**Flujos Alternativos:**
- 2a. Cliente no existe
  - Sistema permite crear cliente nuevo en el proceso
- 5a. Horario no disponible
  - Sistema sugiere horarios libres cercanos
- 8a. Cliente sin email/teléfono
  - Sistema crea turno sin enviar notificación

---

### CU-009: Gestionar Clientes
**Actor Principal:** Profesional  
**Precondiciones:** Usuario autenticado  
**Postcondiciones:** Información de clientes actualizada

**Flujo Principal:**
1. Profesional accede a lista de clientes
2. Sistema muestra clientes paginados con buscador
3. Profesional puede buscar por nombre, email o teléfono
4. Profesional selecciona cliente para ver detalles
5. Sistema muestra historial de turnos del cliente
6. Profesional puede editar información del cliente
7. Sistema guarda cambios y confirma actualización

**Flujos Alternativos:**
- 3a. No se encuentran resultados
  - Sistema ofrece crear nuevo cliente
- 6a. Datos inválidos
  - Sistema muestra errores de validación

---

## **3. Casos de Uso - Administrador de Negocio**

### CU-010: Configurar Negocio
**Actor Principal:** Administrador de Negocio  
**Precondiciones:** Usuario autenticado como propietario  
**Postcondiciones:** Configuración del negocio actualizada

**Flujo Principal:**
1. Administrador accede a configuraciones del negocio
2. Sistema muestra formulario con datos actuales
3. Administrador modifica información (nombre, dirección, contacto)
4. Administrador configura zona horaria
5. Sistema valida datos ingresados
6. Sistema guarda configuración
7. Sistema confirma actualización exitosa

**Flujos Alternativos:**
- 5a. Datos inválidos
  - Sistema muestra errores específicos por campo
- 6a. Error al guardar
  - Sistema muestra mensaje de error y permite reintentar

---

### CU-011: Gestionar Servicios
**Actor Principal:** Administrador de Negocio  
**Precondiciones:** Usuario autenticado con permisos de negocio  
**Postcondiciones:** Catálogo de servicios actualizado

**Flujo Principal:**
1. Administrador accede a gestión de servicios
2. Sistema muestra lista de servicios existentes
3. Administrador puede crear nuevo servicio
4. Administrador completa datos (nombre, duración, precio, descripción)
5. Sistema valida información del servicio
6. Sistema guarda nuevo servicio
7. Servicio queda disponible para reservas

**Flujos Alternativos:**
- 4a. Duración inválida (menor a 15 minutos)
  - Sistema muestra error de validación
- 4b. Precio inválido
  - Sistema solicita precio válido mayor a 0

---

### CU-012: Configurar Horarios de Trabajo
**Actor Principal:** Administrador de Negocio  
**Precondiciones:** Usuario autenticado como propietario  
**Postcondiciones:** Horarios de trabajo configurados

**Flujo Principal:**
1. Administrador accede a configuración de horarios
2. Sistema muestra grilla semanal de horarios
3. Administrador configura horarios por día de la semana
4. Administrador define hora de inicio y fin para cada día
5. Administrador puede marcar días como cerrado
6. Sistema valida consistencia de horarios
7. Sistema guarda configuración de horarios

**Flujos Alternativos:**
- 6a. Horarios inconsistentes (fin antes que inicio)
  - Sistema muestra error y solicita corrección
- 6b. Horarios solapados
  - Sistema detecta conflicto y pide aclaración

---

### CU-013: Gestionar Excepciones de Horarios
**Actor Principal:** Administrador de Negocio  
**Precondiciones:** Usuario autenticado con permisos  
**Postcondiciones:** Excepciones de horarios configuradas

**Flujo Principal:**
1. Administrador accede a gestión de excepciones
2. Sistema muestra calendario con excepciones existentes
3. Administrador selecciona fecha para crear excepción
4. Administrador define si es día cerrado o horario especial
5. Si es horario especial, define horas de inicio y fin
6. Administrador agrega motivo de la excepción
7. Sistema guarda excepción y actualiza disponibilidad

**Flujos Alternativos:**
- 3a. Fecha en el pasado
  - Sistema no permite crear excepción retroactiva
- 4a. Ya existe excepción para la fecha
  - Sistema permite editar excepción existente

---

### CU-014: Gestionar Equipo de Trabajo
**Actor Principal:** Administrador de Negocio  
**Precondiciones:** Usuario es propietario del negocio  
**Postcondiciones:** Equipo de trabajo actualizado

**Flujo Principal:**
1. Administrador accede a gestión de equipo
2. Sistema muestra lista de empleados actuales
3. Administrador puede agregar nuevo empleado por email
4. Sistema envía invitación al email especificado
5. Empleado acepta invitación y se registra
6. Administrador asigna rol (empleado/administrador)
7. Sistema actualiza permisos del usuario

**Flujos Alternativos:**
- 4a. Email ya asociado a otro negocio
  - Sistema permite agregar mismo usuario a múltiples negocios
- 5a. Empleado no acepta invitación
  - Sistema mantiene invitación pendiente por 7 días

---

### CU-015: Ver Reportes y Analytics
**Actor Principal:** Administrador de Negocio  
**Precondiciones:** Usuario autenticado con datos históricos  
**Postcondiciones:** Reportes generados y visualizados

**Flujo Principal:**
1. Administrador accede a sección de reportes
2. Administrador selecciona tipo de reporte (ingresos, citas, clientes)
3. Administrador define rango de fechas
4. Sistema procesa datos históricos
5. Sistema genera gráficos y métricas
6. Sistema muestra dashboard interactivo
7. Administrador puede exportar reportes en PDF/Excel

**Flujos Alternativos:**
- 4a. No hay datos suficientes para el período
  - Sistema muestra mensaje informativo
- 7a. Error en exportación
  - Sistema notifica error y sugiere formato alternativo

---

## **4. Casos de Uso - Sistema Automático**

### CU-016: Enviar Recordatorios Automáticos
**Actor Principal:** Sistema de Notificaciones  
**Precondiciones:** Turnos confirmados para mañana  
**Postcondiciones:** Recordatorios enviados a clientes

**Flujo Principal:**
1. Sistema ejecuta tarea programada diariamente a las 18:00
2. Sistema consulta turnos confirmados para el día siguiente
3. Para cada turno, sistema verifica si ya se envió recordatorio
4. Sistema genera email/SMS de recordatorio personalizado
5. Sistema envía recordatorio al cliente
6. Sistema marca recordatorio como enviado
7. Sistema registra estadísticas de envío

**Flujos Alternativos:**
- 5a. Error al enviar recordatorio
  - Sistema reintenta envío hasta 3 veces
- 5b. Cliente sin email/teléfono válido
  - Sistema registra envío fallido para revisión manual

---

### CU-017: Sincronizar con Google Calendar
**Actor Principal:** Google Calendar API  
**Precondiciones:** Integración configurada y activa  
**Postcondiciones:** Eventos sincronizados en ambas direcciones

**Flujo Principal:**
1. Sistema detecta cambio en turno (creación, modificación, cancelación)
2. Sistema verifica si negocio tiene integración activa
3. Sistema autentica con Google Calendar API
4. Sistema crea/actualiza/elimina evento correspondiente
5. Google Calendar confirma operación
6. Sistema marca sincronización como exitosa

**Flujos Alternativos:**
- 3a. Token de acceso expirado
  - Sistema renueva token usando refresh token
- 4a. Error en API de Google
  - Sistema programa reintento en 15 minutos
- 5a. Conflicto en Google Calendar
  - Sistema notifica al usuario para resolución manual

---

## **5. Casos de Uso - Administrador del Sistema**

### CU-018: Gestionar Usuarios del Sistema
**Actor Principal:** Administrador del Sistema  
**Precondiciones:** Usuario con rol de super administrador  
**Postcondiciones:** Usuarios del sistema gestionados

**Flujo Principal:**
1. Administrador accede a panel de administración
2. Sistema muestra lista de todos los usuarios registrados
3. Administrador puede filtrar por rol, estado, fecha de registro
4. Administrador selecciona usuario para ver detalles
5. Administrador puede activar/desactivar cuentas
6. Administrador puede cambiar roles de usuario
7. Sistema registra todas las acciones administrativas

**Flujos Alternativos:**
- 5a. Usuario tiene negocios activos
  - Sistema advierte sobre impacto antes de desactivar
- 6a. Cambio de rol no permitido
  - Sistema explica restricciones de cambio de rol

---

### CU-019: Monitorear Salud del Sistema
**Actor Principal:** Administrador del Sistema  
**Precondiciones:** Sistema en funcionamiento  
**Postcondiciones:** Estado del sistema evaluado

**Flujo Principal:**
1. Administrador accede a dashboard de monitoreo
2. Sistema muestra métricas en tiempo real
3. Sistema presenta estadísticas de uso (usuarios activos, turnos, errores)
4. Sistema muestra logs de errores recientes
5. Administrador puede investigar problemas específicos
6. Administrador puede ejecutar acciones correctivas

**Flujos Alternativos:**
- 4a. Errores críticos detectados
  - Sistema envía alertas automáticas por email/SMS
- 6a. Acción correctiva requiere reinicio
  - Sistema solicita confirmación debido al impacto

---

## **Matriz de Trazabilidad**

| Caso de Uso | Actor Principal | Prioridad | Complejidad | Estado |
|-------------|----------------|-----------|-------------|---------|
| CU-001 | Cliente | Alta | Baja | Implementado |
| CU-002 | Cliente | Alta | Media | Implementado |
| CU-003 | Cliente | Alta | Alta | Implementado |
| CU-004 | Cliente | Alta | Media | Implementado |
| CU-005 | Cliente | Media | Media | Implementado |
| CU-006 | Profesional | Alta | Baja | Implementado |
| CU-007 | Profesional | Alta | Media | Implementado |
| CU-008 | Profesional | Media | Media | Implementado |
| CU-009 | Profesional | Media | Baja | Implementado |
| CU-010 | Admin Negocio | Alta | Media | Implementado |
| CU-011 | Admin Negocio | Alta | Media | Implementado |
| CU-012 | Admin Negocio | Alta | Alta | Implementado |
| CU-013 | Admin Negocio | Media | Media | Implementado |
| CU-014 | Admin Negocio | Media | Alta | En desarrollo |
| CU-015 | Admin Negocio | Baja | Alta | Planificado |
| CU-016 | Sistema | Alta | Media | Implementado |
| CU-017 | Google API | Media | Alta | En desarrollo |
| CU-018 | Admin Sistema | Baja | Media | Planificado |
| CU-019 | Admin Sistema | Baja | Alta | Planificado |
