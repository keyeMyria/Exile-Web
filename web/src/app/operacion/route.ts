import { Routes } from '@angular/router';
import { MenuMeta, RouteComponent } from '../shared';
import { ClienteEditComponent, ClienteListComponent } from './cliente/cliente.component';
import { LugarEditComponent, LugarListComponent } from './lugar/lugar.component';
import { TareaComponent } from './tarea/tarea.component';
import { TareaListComponent, TareaFormComponent } from './tareas-list/tareas-list.component';
import { CalendarioComponent } from './calendario/calendario.component';

import { ClienteService } from './cliente/cliente.service';
import { LugarService } from './lugar/lugar.service';
import { TareaService } from './tarea/tarea.service';

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
            {
                path: 'tareaday', component: RouteComponent, data: { miga: 'Tareas del Dia' }, children: [
                    { path: '', component: TareaComponent },
                ]
            },
            {
                path: 'tarea', component: RouteComponent, data: { miga: 'Tareas' }, children: [
                    { path: '', component: TareaListComponent },
                    {
                        path: ':id/edit', component: TareaFormComponent,
                        data: { miga: 'Editar' },
                        resolve: { item: TareaService }
                    }
                ]
            },
            { path: 'calendario', component: CalendarioComponent, data: { miga: 'Calendario' }, children: [] }
        ]
    }

];

export const OperacionMenuMeta: MenuMeta[] = [
    { title: 'Clientes', url: '/operacion/cliente' },
    { title: 'Lugares de Trabajo', url: '/operacion/lugar' },
    { title: 'Tareas del dia ', url: '/operacion/tareaday' },
    { title: 'Tareas', url: '/operacion/tarea' },
    { title: 'Calendario', url: '/operacion/calendario' }
];
