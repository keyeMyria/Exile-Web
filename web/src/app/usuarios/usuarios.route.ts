import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { AsistenteComponent, AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
import { EmpleadoComponent } from './empleado/empleado.component';



export const UsuariosRoutes: Routes = [
    {
        path: '', children: [
            { path: 'asistente', component: AsistenteComponent, children: [
                { path: '', component: AsistenteListComponent},
                { path: 'edit', component: AsistenteEditComponent}
            ]},
            { path: 'empleado', component: EmpleadoComponent },
        ]
    }
];


export const UsuariosMenuMeta: MenuMeta[] = [
    { title: 'Asistente', url: '/usuarios/asistente', icon: 'supervisor_account' },
    { title: 'Empleado', url: '/usuarios/empleado', icon: 'account_box' }
];
