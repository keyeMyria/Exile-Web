import { Routes } from '@angular/router';
import { MenuMeta, RouteComponent } from 'componentex';
import { TipoclienteListComponent, TipoclienteEditComponent } from './tipocliente/tipocliente.component';
import { ClienteEditComponent, ClienteListComponent } from './cliente/cliente.component';
import { TipoclienteService } from './tipocliente/tipocliente.service';
import { ClienteService } from './cliente/cliente.service';
export const OperacionRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'tipo/cliente', component: RouteComponent, data: { miga: 'Tipo de cliente' }, children: [
                    { path: '', component: TipoclienteListComponent },
                    {
                        path: ':id/edit', component: TipoclienteEditComponent,
                        data: { miga: 'Editar' },
                        resolve: { item: TipoclienteService }
                    }
                ]
            },
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
            { path: 'lugar', component: RouteComponent, data: { miga: 'Lugares de Trabajo' }, children: [] },
            { path: 'tarea', component: RouteComponent, data: { miga: 'Tareas' }, children: [] },
            { path: 'calendario', component: RouteComponent, data: { miga: 'Calendario' }, children: [] }
        ]
    }

];

export const OperacionMenuMeta: MenuMeta[] = [
    { title: 'Cliente', url: '/operacion/cliente' },
    { title: 'Tipo de Cliente', url: '/operacion/tipo/cliente' },
    { title: 'Lugares de Trabajo', url: '/operacion/lugar' },
    { title: 'Tareas', url: '/operacion/tarea' },
    { title: 'Calendario', url: '/operacion/calendario' }
];
