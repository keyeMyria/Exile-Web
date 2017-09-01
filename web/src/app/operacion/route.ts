import { Routes } from '@angular/router';
import { MenuMeta, RouteComponent } from 'componentex';
import { ClienteEditComponent, ClienteListComponent } from './cliente/cliente.component';
import { LugarEditComponent, LugarListComponent } from './lugar/lugar.component';

import { ClienteService } from './cliente/cliente.service';
import { LugarService } from './lugar/lugar.service';

export const OperacionRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'cliente', component: RouteComponent, data: { miga: 'Cliente' }, children: [
                    { path: '', component: ClienteListComponent },
                    {
                        path: ':id/edit', component: ClienteEditComponent,
                        data: { miga: 'Editar' },
                        resolve: { item: ClienteService }
                    }
                ]
            },
            {
                path: 'lugar', component: RouteComponent, data: { miga: 'Lugares de Trabajo' }, children: [
                    { path: '', component: LugarListComponent },
                    {
                        path: ':id/edit', component: LugarEditComponent,
                        data: { miga: 'Editar' },
                        resolve: { item: LugarService }
                    }
                ]
            },
            { path: 'tarea', component: RouteComponent, data: { miga: 'Tareas' }, children: [] },
            { path: 'calendario', component: RouteComponent, data: { miga: 'Calendario' }, children: [] }
        ]
    }

];

export const OperacionMenuMeta: MenuMeta[] = [
    { title: 'Clientes', url: '/operacion/cliente' },
    { title: 'Lugares de Trabajo', url: '/operacion/lugar' },
    { title: 'Tareas', url: '/operacion/tarea' },
    { title: 'Calendario', url: '/operacion/calendario' }
];
