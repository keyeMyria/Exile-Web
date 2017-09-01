import { Routes } from '@angular/router';
import { MenuMeta, RouteComponent } from 'componentex';
import { AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
import { AsistenteService } from './asistente/asistente.service';
import { EditEmpleadoComponent, ListEmpleadoComponent } from './empleado/empleado.component';
import { EmpleadoService } from './empleado/empleado.service';


export const UsuariosRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'empleado', component: RouteComponent, data: { miga: 'Empleado' }, children: [
                    { path: '', component: ListEmpleadoComponent },
                    { path: ':id/edit', component: EditEmpleadoComponent, data: { miga: 'Editar' }, resolve: { item: EmpleadoService } }
                ]
            },
            {
                path: 'asistente', component: RouteComponent, data: { miga: 'Asistente' }, children: [
                    { path: '', component: AsistenteListComponent },
                    { path: ':id/edit', component: AsistenteEditComponent, data: { miga: 'Editar' }, resolve: { item: AsistenteService } }
                ]
            },

        ]
    }

];

export const UsuariosMenuMeta: MenuMeta[] = [
    { title: 'Asistente', url: '/usuarios/asistente', icon: 'supervisor_account' },
    { title: 'Empleado', url: '/usuarios/empleado', icon: 'account_box' },
];
