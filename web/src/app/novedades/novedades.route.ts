import { Routes } from '@angular/router';

import { ReportesComponent } from './reportes/reportes.component';
import { NotificacionesComponent } from './notificaciones/notificaciones.component';
import { ChatComponent } from './chat/chat.component';

export const NovedadesRoutes: Routes = [
    {
        path: '', children: [
            { path: 'reportes', component: ReportesComponent },
            { path: 'notificaciones', component: NotificacionesComponent },
            { path: 'chat', component: ChatComponent },
        ]
    }
];
