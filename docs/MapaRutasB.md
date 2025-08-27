## API REST Endpoints - TurnoPlus Backend

### Base URL
```
Production: https://api.turnoplus.com/v1
Development: http://localhost:3000/api/v1
```

### Autenticación
- **Tipo**: Bearer Token (JWT)
- **Header**: `Authorization: Bearer <token>`
- **Expiración**: 24 horas (configurable)

---

## 1. **Autenticación y Usuarios** `/auth`

### Autenticación Pública
```http
POST   /auth/login                    # Iniciar sesión
POST   /auth/register                 # Registrar nuevo usuario
POST   /auth/refresh                  # Renovar token
POST   /auth/logout                   # Cerrar sesión
POST   /auth/forgot-password          # Solicitar recuperación de contraseña
POST   /auth/reset-password           # Restablecer contraseña
GET    /auth/verify-email/:token      # Verificar email
```

### Gestión de Perfil (Requiere autenticación)
```http
GET    /auth/me                       # Obtener perfil del usuario actual
PUT    /auth/me                       # Actualizar perfil del usuario
PUT    /auth/change-password          # Cambiar contraseña
DELETE /auth/me                       # Eliminar cuenta
```

---

## 2. **Negocios** `/businesses`

### Gestión de Negocios
```http
GET    /businesses                    # Listar negocios del usuario actual
POST   /businesses                    # Crear nuevo negocio
GET    /businesses/:id                # Obtener detalles de un negocio
PUT    /businesses/:id                # Actualizar negocio
DELETE /businesses/:id                # Eliminar negocio
PATCH  /businesses/:id/status         # Activar/desactivar negocio
```

### Configuraciones del Negocio
```http
GET    /businesses/:id/settings       # Obtener configuraciones
PUT    /businesses/:id/settings       # Actualizar configuraciones
GET    /businesses/:id/settings/:key  # Obtener configuración específica
PUT    /businesses/:id/settings/:key  # Actualizar configuración específica
```

### Gestión de Empleados
```http
GET    /businesses/:id/users          # Listar usuarios del negocio
POST   /businesses/:id/users          # Agregar usuario al negocio
PUT    /businesses/:id/users/:userId  # Actualizar rol de usuario
DELETE /businesses/:id/users/:userId  # Remover usuario del negocio
```

---

## 3. **Servicios** `/businesses/:businessId/services`

### CRUD de Servicios
```http
GET    /businesses/:businessId/services           # Listar servicios
POST   /businesses/:businessId/services           # Crear servicio
GET    /businesses/:businessId/services/:id       # Obtener servicio
PUT    /businesses/:businessId/services/:id       # Actualizar servicio
DELETE /businesses/:businessId/services/:id       # Eliminar servicio
PATCH  /businesses/:businessId/services/:id/status # Activar/desactivar servicio
```

---

## 4. **Horarios y Disponibilidad** `/businesses/:businessId/schedules`

### Horarios Regulares
```http
GET    /businesses/:businessId/schedules          # Obtener horarios semanales
PUT    /businesses/:businessId/schedules          # Actualizar horarios semanales
GET    /businesses/:businessId/schedules/:day     # Obtener horario de un día
PUT    /businesses/:businessId/schedules/:day     # Actualizar horario de un día
```

### Excepciones de Horarios
```http
GET    /businesses/:businessId/exceptions         # Listar excepciones
POST   /businesses/:businessId/exceptions         # Crear excepción
GET    /businesses/:businessId/exceptions/:id     # Obtener excepción
PUT    /businesses/:businessId/exceptions/:id     # Actualizar excepción
DELETE /businesses/:businessId/exceptions/:id     # Eliminar excepción
```

### Disponibilidad Pública
```http
GET    /businesses/:businessId/availability       # Obtener disponibilidad
GET    /businesses/:businessId/availability/:date # Disponibilidad de fecha específica
GET    /businesses/:businessId/slots              # Slots disponibles para reserva
```

---

## 5. **Turnos/Citas** `/appointments`

### Gestión de Turnos (Admin/Professional)
```http
GET    /appointments                  # Listar turnos (con filtros)
POST   /appointments                  # Crear turno manualmente
GET    /appointments/:id              # Obtener detalles del turno
PUT    /appointments/:id              # Actualizar turno
DELETE /appointments/:id              # Eliminar turno
```

### Estados de Turnos
```http
PATCH  /appointments/:id/confirm      # Confirmar turno
PATCH  /appointments/:id/cancel       # Cancelar turno
PATCH  /appointments/:id/complete     # Marcar como completado
PATCH  /appointments/:id/no-show      # Marcar como no presentado
```

### Reservas Públicas (Sin autenticación)
```http
POST   /public/appointments           # Crear reserva pública
GET    /public/appointments/:token/confirm # Confirmar reserva por token
PATCH  /public/appointments/:token/cancel  # Cancelar reserva por token
```

---

## 6. **Clientes** `/customers`

### Gestión de Clientes
```http
GET    /customers                     # Listar clientes
POST   /customers                     # Crear cliente
GET    /customers/:id                 # Obtener cliente
PUT    /customers/:id                 # Actualizar cliente
DELETE /customers/:id                 # Eliminar cliente
GET    /customers/:id/appointments    # Historial de citas del cliente
```

### Búsqueda de Clientes
```http
GET    /customers/search              # Buscar clientes por nombre/email/teléfono
```

---

## 7. **Notificaciones** `/notifications`

### Gestión de Notificaciones
```http
GET    /notifications                 # Listar notificaciones del usuario
GET    /notifications/:id             # Obtener notificación específica
PATCH  /notifications/:id/read        # Marcar como leída
PATCH  /notifications/mark-all-read   # Marcar todas como leídas
DELETE /notifications/:id             # Eliminar notificación
```

### Configuración de Notificaciones
```http
GET    /notifications/settings        # Obtener preferencias de notificación
PUT    /notifications/settings        # Actualizar preferencias
```

---

## 8. **Integraciones** `/integrations`

### Google Calendar
```http
GET    /integrations/google-calendar          # Estado de integración
POST   /integrations/google-calendar/connect  # Conectar con Google Calendar
DELETE /integrations/google-calendar/disconnect # Desconectar Google Calendar
POST   /integrations/google-calendar/sync     # Sincronizar eventos
```

---

## 9. **Reportes y Analytics** `/reports`

### Reportes de Negocio
```http
GET    /reports/appointments           # Reporte de citas
GET    /reports/revenue               # Reporte de ingresos
GET    /reports/customers             # Reporte de clientes
GET    /reports/services              # Reporte de servicios más solicitados
GET    /reports/dashboard             # Datos del dashboard principal
```

### Filtros de Reportes
- `?start_date=YYYY-MM-DD`
- `?end_date=YYYY-MM-DD`
- `?business_id=number`
- `?service_id=number`
- `?status=enum`

---

## 10. **Administración del Sistema** `/admin`

### Gestión de Usuarios (Solo Super Admin)
```http
GET    /admin/users                   # Listar todos los usuarios
GET    /admin/users/:id               # Obtener usuario específico
PATCH  /admin/users/:id/status        # Activar/desactivar usuario
DELETE /admin/users/:id               # Eliminar usuario
```

### Gestión de Negocios (Solo Super Admin)
```http
GET    /admin/businesses              # Listar todos los negocios
PATCH  /admin/businesses/:id/status   # Activar/desactivar negocio
DELETE /admin/businesses/:id          # Eliminar negocio
```

---

## **Códigos de Estado HTTP**

### Códigos de Éxito
- `200 OK` - Operación exitosa
- `201 Created` - Recurso creado exitosamente
- `204 No Content` - Operación exitosa sin contenido de respuesta

### Códigos de Error del Cliente
- `400 Bad Request` - Solicitud malformada o datos inválidos
- `401 Unauthorized` - No autenticado o token inválido
- `403 Forbidden` - Sin permisos para acceder al recurso
- `404 Not Found` - Recurso no encontrado
- `409 Conflict` - Conflicto con el estado actual del recurso
- `422 Unprocessable Entity` - Errores de validación

### Códigos de Error del Servidor
- `500 Internal Server Error` - Error interno del servidor
- `503 Service Unavailable` - Servicio temporalmente no disponible

---

## **Middleware y Validaciones**

### Middleware de Autenticación
```javascript
// Rutas que requieren autenticación
authenticate: [
  '/auth/me', '/businesses/*', '/appointments/*', 
  '/customers/*', '/notifications/*', '/reports/*'
]

// Rutas públicas
public: [
  '/auth/login', '/auth/register', '/public/*',
  '/businesses/:id/availability', '/businesses/:id/slots'
]
```

### Middleware de Autorización
```javascript
// Solo propietarios de negocio
businessOwner: ['/businesses/:id', '/businesses/:id/users']

// Propietarios y empleados
businessMember: ['/businesses/:id/services', '/appointments']

// Solo administradores del sistema
systemAdmin: ['/admin/*']
```

### Validaciones de Input
- **Validación de emails**: RFC 5322 compliant
- **Validación de teléfonos**: Formato internacional
- **Validación de fechas**: ISO 8601 format
- **Validación de horarios**: Formato HH:MM en 24h
- **Sanitización**: XSS protection, SQL injection prevention

### Rate Limiting
```javascript
// Límites por endpoint
publicRoutes: 100 requests/hour per IP
authenticatedRoutes: 1000 requests/hour per user
emailSending: 10 emails/hour per business
```