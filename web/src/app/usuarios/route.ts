import { Routes } from '@angular/router';
import { MenuMeta } from 'componentex';
import { AsistenteComponent, AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
import { AdminComponent, EditAdminComponent, ListAdminComponent } from './admin/admin.component';
import { AsistenteService } from './asistente/asistente.service';
import { AdminService } from './admin/admin.service';

export const UsuariosRoutes: Routes = [
    {
        path: '', children: [
            // {
            //     path: 'admin', component: AdminComponent, data: { miga: 'Administrador' }, children: [
            //         { path: '', component: ListAdminComponent },
            //         { path: ':id/edit', component: EditAdminComponent, data: { miga: 'Editar' }, resolve: { item: AdminService } }
            //     ]
            // },
            {
                path: 'asistente', component: AsistenteComponent, data: { miga: 'Asistente' }, children: [
                    { path: '', component: AsistenteListComponent },
                    { path: ':id/edit', component: AsistenteEditComponent, data: { miga: 'Editar' }, resolve: { item: AsistenteService } }
                ]
            },
        ]
    }

];

export const UsuariosMenuMeta: MenuMeta[] = [
    // { title: 'Administrador', url: '/usuarios/admin', icon: 'account_box' },
    { title: 'Asistente', url: '/usuarios/asistente', icon: 'supervisor_account' },
];
