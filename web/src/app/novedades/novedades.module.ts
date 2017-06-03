import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { NovedadesRoutes } from './novedades.route';
import { ReportesComponent } from './reportes/reportes.component';
import { NotificacionesComponent } from './notificaciones/notificaciones.component';
import { ChatComponent } from './chat/chat.component';

@NgModule({
    imports: [
        RouterModule.forChild(NovedadesRoutes),
        CommonModule
    ],
    declarations: [ReportesComponent, NotificacionesComponent, ChatComponent],
    providers: []
})
export class NovedadesModule { }
