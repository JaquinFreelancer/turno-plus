## Frontend Routes - TurnoPlus SPA

### Tecnología Base
```
Framework: React 18+ / Vue 3+ / Angular 15+
Router: React Router / Vue Router / Angular Router
State Management: Redux Toolkit / Pinia / NgRx
UI Framework: Tailwind CSS + Headless UI
```

---

## 1. **Rutas Públicas** (Sin autenticación requerida)

### Landing y Marketing
```javascript
/                           # Página de inicio/landing
/about                      # Acerca de nosotros
/features                   # Características del producto
/pricing                    # Planes y precios
/contact                    # Contacto y soporte
/help                       # Centro de ayuda/FAQ
/terms                      # Términos y condiciones
/privacy                    # Política de privacidad
```

### Autenticación
```javascript
/login                      # Página de inicio de sesión
/register                   # Registro de nuevos usuarios
/forgot-password            # Recuperación de contraseña
/reset-password/:token      # Restablecer contraseña
/verify-email/:token        # Verificación de email
```

### Reservas Públicas
```javascript
/book/:businessSlug         # Página pública de reservas
/book/:businessSlug/confirm # Confirmación de reserva
/appointment/confirm/:token # Confirmar cita por email
/appointment/cancel/:token  # Cancelar cita por email
```

---

## 2. **Rutas Privadas** (Requieren autenticación)

### Dashboard Principal
```javascript
/dashboard                  # Dashboard principal del usuario
/dashboard/overview         # Vista general de métricas
/dashboard/calendar         # Vista de calendario general
/dashboard/notifications    # Centro de notificaciones
```

---

## 3. **Gestión de Negocios** `/business`

### CRUD de Negocios
```javascript
/business                   # Lista de negocios del usuario
/business/new               # Crear nuevo negocio
/business/:id               # Vista general del negocio
/business/:id/edit          # Editar información del negocio
/business/:id/settings      # Configuraciones del negocio
```

### Gestión Operativa
```javascript
/business/:id/dashboard     # Dashboard específico del negocio
/business/:id/calendar      # Calendario del negocio
/business/:id/appointments  # Lista de citas del negocio
/business/:id/customers     # Gestión de clientes
/business/:id/services      # Gestión de servicios
/business/:id/schedule      # Configuración de horarios
/business/:id/team          # Gestión de equipo/empleados
```

### Reportes y Analytics
```javascript
/business/:id/reports       # Hub de reportes
/business/:id/reports/appointments    # Reporte de citas
/business/:id/reports/revenue        # Reporte de ingresos
/business/:id/reports/customers      # Análisis de clientes
/business/:id/reports/services       # Rendimiento de servicios
```

---

## 4. **Gestión de Servicios** `/business/:id/services`

### CRUD de Servicios
```javascript
/business/:id/services              # Lista de servicios
/business/:id/services/new          # Crear nuevo servicio
/business/:id/services/:serviceId   # Detalles del servicio
/business/:id/services/:serviceId/edit    # Editar servicio
```

---

## 5. **Gestión de Citas** `/appointments`

### Vistas de Citas
```javascript
/appointments               # Lista global de citas del usuario
/appointments/new           # Crear nueva cita manualmente
/appointments/:id           # Detalles de la cita
/appointments/:id/edit      # Editar cita
/appointments/calendar      # Vista de calendario de citas
```

### Filtros y Vistas Especializadas
```javascript
/appointments/today         # Citas de hoy
/appointments/pending       # Citas pendientes de confirmación
/appointments/confirmed     # Citas confirmadas
/appointments/completed     # Citas completadas
/appointments/cancelled     # Citas canceladas
```

---

## 6. **Gestión de Clientes** `/customers`

### CRUD de Clientes
```javascript
/customers                  # Lista de clientes
/customers/new              # Agregar nuevo cliente
/customers/:id              # Perfil del cliente
/customers/:id/edit         # Editar información del cliente
/customers/:id/history      # Historial de citas del cliente
```

### Funciones Avanzadas
```javascript
/customers/search           # Búsqueda avanzada de clientes
/customers/import           # Importar clientes (CSV/Excel)
/customers/export           # Exportar clientes
```

---

## 7. **Configuraciones** `/settings`

### Configuraciones de Usuario
```javascript
/settings                   # Hub de configuraciones
/settings/profile           # Configuración de perfil
/settings/account           # Configuración de cuenta
/settings/notifications     # Preferencias de notificaciones
/settings/security          # Configuraciones de seguridad
```

### Configuraciones de Negocio
```javascript
/settings/business/:id      # Configuraciones del negocio
/settings/business/:id/general        # Información general
/settings/business/:id/schedule       # Horarios de trabajo
/settings/business/:id/notifications  # Configuración de notificaciones
/settings/business/:id/integrations   # Integraciones externas
/settings/business/:id/billing        # Facturación y pagos
```

---

## 8. **Integraciones** `/integrations`

### Google Calendar
```javascript
/integrations               # Hub de integraciones
/integrations/google-calendar         # Configuración Google Calendar
/integrations/google-calendar/setup   # Configurar integración
/integrations/google-calendar/sync    # Sincronización manual
```

### Futuras Integraciones
```javascript
/integrations/outlook       # Microsoft Outlook (futuro)
/integrations/zoom          # Zoom meetings (futuro)
/integrations/payments      # Pasarelas de pago (futuro)
```

---

## 9. **Notificaciones** `/notifications`

### Centro de Notificaciones
```javascript
/notifications              # Centro de notificaciones
/notifications/unread       # Notificaciones no leídas
/notifications/settings     # Configurar notificaciones
```

---

## 10. **Ayuda y Soporte** `/help`

### Documentación y Soporte
```javascript
/help                       # Centro de ayuda
/help/getting-started       # Guía de inicio
/help/tutorials             # Tutoriales paso a paso
/help/faq                   # Preguntas frecuentes
/help/contact               # Contactar soporte
/help/feedback              # Enviar feedback
```

---

## **Rutas Administrativas** `/admin` (Solo Super Admin)

### Administración del Sistema
```javascript
/admin                      # Dashboard administrativo
/admin/users                # Gestión de usuarios
/admin/users/:id            # Detalles de usuario
/admin/businesses           # Gestión de negocios
/admin/businesses/:id       # Detalles de negocio
/admin/system               # Configuraciones del sistema
/admin/analytics            # Analytics globales
```

---

## **Protección de Rutas y Guards**

### Guard de Autenticación
```javascript
// Rutas que requieren login
const protectedRoutes = [
  '/dashboard/*',
  '/business/*',
  '/appointments/*',
  '/customers/*',
  '/settings/*',
  '/integrations/*',
  '/notifications/*',
  '/admin/*'
];

// Middleware de redirección
const authGuard = (to, from, next) => {
  const token = getAuthToken();
  if (!token) {
    next('/login?redirect=' + to.path);
  } else {
    next();
  }
};
```

### Guard de Roles
```javascript
// Control de acceso por roles
const roleGuards = {
  businessOwner: ['/business/:id/team', '/business/:id/settings'],
  businessMember: ['/business/:id/*'],
  systemAdmin: ['/admin/*']
};

const roleGuard = (requiredRole) => {
  return (to, from, next) => {
    const userRole = getUserRole();
    if (hasPermission(userRole, requiredRole)) {
      next();
    } else {
      next('/dashboard'); // Redirect to safe area
    }
  };
};
```

### Guard de Verificación de Email
```javascript
const emailVerificationGuard = (to, from, next) => {
  const user = getCurrentUser();
  const protectedRoutes = ['/business/new', '/integrations/*'];
  
  if (protectedRoutes.some(route => to.path.match(route)) && !user.emailVerified) {
    next('/verify-email-required');
  } else {
    next();
  }
};
```

---

## **Estructura de Componentes de Página**

### Layout Components
```javascript
// Layouts principales
AppLayout              # Layout base con header/footer
DashboardLayout        # Layout con sidebar para dashboard
BusinessLayout         # Layout específico para gestión de negocio
PublicLayout          # Layout para páginas públicas
AuthLayout            # Layout para autenticación
```

### Page Components
```javascript
// Estructura de componentes por página
HomePage
  ├── HeroSection
  ├── FeaturesSection
  ├── TestimonialsSection
  └── CTASection

DashboardPage
  ├── StatsCards
  ├── RecentAppointments
  ├── TodaySchedule
  └── QuickActions

BusinessCalendarPage
  ├── CalendarHeader
  ├── CalendarGrid
  ├── AppointmentModal
  └── TimeSlotSelector
```

---

## **Estados de Carga y Error**

### Loading States
```javascript
/loading                # Página de carga inicial
/business/:id/loading   # Carga específica de negocio
```

### Error Pages
```javascript
/404                    # Página no encontrada
/403                    # Acceso denegado
/500                    # Error interno del servidor
/offline                # Sin conexión a internet
/maintenance            # Página de mantenimiento
```

---

## **Rutas Dinámicas y Parámetros**

### Parámetros de URL
```javascript
// Parámetros principales
:id                     # ID de entidad (business, appointment, customer)
:businessSlug           # Slug público del negocio
:token                  # Tokens de confirmación/reset
:serviceId              # ID de servicio específico

// Query Parameters
?date=YYYY-MM-DD       # Filtro de fecha
?status=pending        # Filtro de estado
?search=query          # Término de búsqueda
?page=1               # Paginación
?redirect=path        # Redirección post-login
```

### Navegación Programática
```javascript
// Ejemplos de navegación
navigateToAppointment(appointmentId)
navigateToBusiness(businessId)
navigateToCalendar(date)
navigateWithFilters(filters)
```

---

## **Responsive Design y Mobile**

### Breakpoints
```css
mobile: 320px - 767px     # Vistas móviles optimizadas
tablet: 768px - 1023px    # Vistas de tablet
desktop: 1024px+          # Vistas de escritorio
```

### Mobile-First Routes
```javascript
// Rutas optimizadas para móvil
/m/book/:businessSlug     # Versión móvil de reservas
/m/calendar              # Calendario móvil optimizado
/m/appointments          # Lista móvil de citas
```