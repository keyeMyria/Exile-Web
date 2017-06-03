import { Routes } from '@angular/router';

import { BaseComponent } from './lib/base/base.component';
import { P404Component } from './lib/404/404.component';
import { AuthComponent } from './auth/auth.component';
import { AuthGuard } from './auth/auth.guard';

export interface MenuMeta {
    title: string;
    url: string;
    icon: string;
    children: MenuMeta[];
}

export const AppRoutes: Routes = [
    { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
    {
        path: '', component: AuthComponent, children: [
            { path: '', loadChildren: './auth/auth.module#AuthModule' }
        ]
    },
    {
        path: '', component: BaseComponent, canActivate: [AuthGuard], children: [
            { path: '', loadChildren: './home/home.module#HomeModule' },
            { path: 'usuarios', loadChildren: './usuarios/usuarios.module#UsuariosModule' },
            { path: 'operacion', loadChildren: './operacion/operacion.module#OperacionModule' },
            { path: 'novedades', loadChildren: './novedades/novedades.module#NovedadesModule' },
            { path: 'informes', loadChildren: './informes/informes.module#InformesModule' },
            { path: 'perfil', loadChildren: './usuarios/usuarios.module#UsuariosModule' },
        ]
    },
    { path: '**', component: P404Component }
];

export const AppMenuMeta: MenuMeta[] = [
    { title: 'Usuarios', url: '', icon: '', children: null },
    { title: 'Operación', url: '', icon: '', children: null },
    { title: 'Novedades', url: '', icon: '', children: null }
];
