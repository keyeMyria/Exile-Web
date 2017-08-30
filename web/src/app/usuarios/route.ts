import { Routes } from '@angular/router';
import { MenuMeta, RouteComponent } from 'componentex';
import { AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
import { AsistenteService } from './asistente/asistente.service';
import { EditEmpleadoComponent, ListEmpleadoComponent } from './empleado/empleado.component';
import { EmpleadoService } from './empleado/empleado.service';
import { CargoListComponent, EditCargoComponent } from './cargo/cargo.component';
import { CargoService } from './cargo/cargo.service';

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
    { title: 'Cargo', url: '/usuarios/cargo', icon: 'turned_in' },
    { title: 'Empleado', url: '/usuarios/empleado', icon: 'account_box' },

];
