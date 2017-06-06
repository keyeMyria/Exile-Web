import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
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


export const UsuariosMenuMeta: MenuMeta[] = [
    { title: 'Asistente', url: '/usuarios/asistente', icon: 'assistant' },
    { title: 'Empleado', url: '/usuarios/empleado', icon: 'account_box' }
];
