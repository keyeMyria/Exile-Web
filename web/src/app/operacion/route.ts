import { Routes } from '@angular/router';
import { MenuMeta } from 'componentex';

export const OperacionRoutes: Routes = [
    {
        path: '', children: [
            // {
            //     path: 'admin', component: AdminComponent, data: { miga: 'Administrador' }, children: [
            //         { path: '', component: ListAdminComponent },
            //         { path: ':id/edit', component: EditAdminComponent, data: { miga: 'Editar' }, resolve: { item: AdminService } }
            //     ]
            // },
            // {
            //     path: 'asistente', component: AsistenteComponent, data: { miga: 'Asistente' }, children: [
            //         { path: '', component: AsistenteListComponent },
            //         {
            //             path: ':id/edit', component: AsistenteEditComponent,
            //             data: { miga: 'Editar' }, resolve: { item: AsistenteService }
            //         }
            //     ]
            // },
        ]
    }

];

export const OperacionMenuMeta: MenuMeta[] = [
    { title: 'Tipo de Cliente', url: '/operacion/tipo/cliente' },
    // { title: 'Asistente', url: '/usuarios/asistente', icon: 'supervisor_account' },
];
