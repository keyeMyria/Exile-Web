import { Routes } from '@angular/router';

import { PerfilComponent } from './perfil/perfil.component';
import { ConfiguracionComponent } from './configuracion/configuracion.component';
import { PlanComponent } from './plan/plan.component';
import { SugerenciasComponent } from './sugerencias/sugerencias.component';
import { HelpComponent } from './help/help.component';

export const PerfilRoutes: Routes = [
    {
        path: '', children: [
            { path: 'miperfil', component: PerfilComponent },
            { path: 'configuracion', component: ConfiguracionComponent },
            { path: 'plan', component: PlanComponent },
            { path: 'sugerencia', component: SugerenciasComponent },
            { path: 'help', component: HelpComponent },
        ]
    }
];
