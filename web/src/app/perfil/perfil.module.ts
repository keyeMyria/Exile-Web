import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { PerfilRoutes } from './perfil.route';
import { PerfilComponent } from './perfil/perfil.component';
import { ConfiguracionComponent } from './configuracion/configuracion.component';
import { PlanComponent } from './plan/plan.component';
import { SugerenciasComponent } from './sugerencias/sugerencias.component';
import { HelpComponent } from './help/help.component';

@NgModule({
    imports: [
        RouterModule.forChild(PerfilRoutes),
        CommonModule
    ],
    declarations: [
        PerfilComponent,
        ConfiguracionComponent,
        PlanComponent,
        SugerenciasComponent,
        HelpComponent
    ],
    providers: []
})
export class PerfilModule { }
