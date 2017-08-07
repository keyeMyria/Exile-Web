import { Routes } from '@angular/router';
import { BaseComponent } from '../lib/base/base.component';
import { P404Component } from '../lib/404/404.component';
import { AuthGuard } from './auth/auth.guard';

export interface MenuMeta {
    title: string;
    icon: string;
    url?: string;
    children?: MenuMeta[];
}

export const AppRoutes: Routes = [
    { path: '', redirectTo: 'operacion/turno', pathMatch: 'full' },
    {
        path: '', component: BaseComponent, canActivate: [AuthGuard], data: { preload: true }, children: [
            { path: '', loadChildren: './home/home.module#HomeModule' },
            { path: 'usuarios', loadChildren: './usuarios/usuarios.module#UsuariosModule' },
        ]
    },
    // { path: '**', component: P404Component }
];

import { UsuariosMenuMeta } from './usuarios/route';

export const AppMenuMeta: MenuMeta[] = [
    { title: 'Inico', url: '/dashboard', icon: 'dashboard' },
    { title: 'Usuarios', icon: 'supervisor_account', children: UsuariosMenuMeta }
];
