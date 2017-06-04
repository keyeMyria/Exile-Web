import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { OperacionRoutes } from './operacion.route';
import { ClienteComponent } from './cliente/cliente.component';
import { LugaresComponent } from './lugares/lugares.component';
import { TareasComponent } from './tareas/tareas.component';
import { CalendarioComponent } from './calendario/calendario.component';

@NgModule({
    imports: [
        RouterModule.forChild(OperacionRoutes),
        CommonModule
    ],
    declarations: [ClienteComponent, LugaresComponent, TareasComponent, CalendarioComponent],
    providers: []
})
export class OperacionModule { }
