import { Routes } from '@angular/router';
import { MenuMeta, RouteComponent } from 'componentex';
import { AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
import { AdminComponent, EditAdminComponent, ListAdminComponent } from './admin/admin.component';
import { AsistenteService } from './asistente/asistente.service';
import { AdminService } from './admin/admin.service';
import { CargoListComponent, EditCargoComponent } from './cargo/cargo.component';
import { CargoService } from './cargo/cargo.service';

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
                path: 'asistente', component: RouteComponent, data: { miga: 'Asistente' }, children: [
                    { path: '', component: AsistenteListComponent },
                    { path: ':id/edit', component: AsistenteEditComponent, data: { miga: 'Editar' }, resolve: { item: AsistenteService } }
                ]
            },
            {
                path: 'cargo', component: RouteComponent, data: { miga: 'Cargo' }, children: [
                    { path: '', component: CargoListComponent },
                    { path: ':id/edit', component: EditCargoComponent, data: { miga: 'Editar' }, resolve: { item: CargoService } }
                ]
            }
        ]
    }

];

export const UsuariosMenuMeta: MenuMeta[] = [
    { title: 'Asistente', url: '/usuarios/asistente', icon: 'supervisor_account' },
    // { title: 'Administrador', url: '/usuarios/admin', icon: 'account_box' },
    { title: 'Cargo', url: '/usuarios/cargo', icon: 'turned_in' },

];
