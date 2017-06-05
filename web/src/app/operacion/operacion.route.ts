import { Routes } from '@angular/router';

import { ClienteComponent } from './cliente/cliente.component';
import { LugaresComponent } from './lugares/lugares.component';
import { TareasComponent } from './tareas/tareas.component';
import { CalendarioComponent } from './calendario/calendario.component';


export const OperacionRoutes: Routes = [
    {
        path: '', children: [
            { path: 'clientes', component: ClienteComponent },
            { path: 'lugares', component: LugaresComponent },
            { path: 'tareas', component: TareasComponent },
            { path: 'calendario', component: CalendarioComponent },
        ]
    }
];
