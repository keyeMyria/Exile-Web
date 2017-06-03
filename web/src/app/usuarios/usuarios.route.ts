import { Routes } from '@angular/router';

import { AsistenteComponent } from './asistente/asistente.component';
import { EmpleadoComponent } from './empleado/empleado.component';


export const UsuariosRoutes: Routes = [
    {
        path: '', children: [
            { path: 'asistente', component: AsistenteComponent },
            { path: 'empleado', component: EmpleadoComponent },
        ]
    }
];
