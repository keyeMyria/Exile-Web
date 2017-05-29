import { Routes } from '@angular/router';

import { BaseComponent } from './containers/pages/base/base.component';
import { AuthComponent } from './containers/pages/auth/auth.component';
import { P404Component } from './containers/pages/404/404.component';
import { AuthGuard } from './containers/pages/auth/auth.guard';

export const AppRoutes: Routes = [
    { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
    {
        path: '', component: AuthComponent, children: [
            { path: '', loadChildren: './containers/pages/auth/auth.module#AuthModule' }
        ]
    },
    {
        path: '', component: BaseComponent, canActivate:[ AuthGuard ],  children: [
            { path: '', loadChildren: './containers/sectios/home/home.module#HomeModule' },
            { path: 'usuarios', loadChildren: './containers/sectios/usuarios/usuarios.module#UsuariosModule' },
            { path: 'operacion', loadChildren: './containers/sectios/operacion/operacion.module#OperacionModule' },
            { path: 'novedades', loadChildren: './containers/sectios/novedades/novedades.module#NovedadesModule' },
            { path: 'informes', loadChildren: './containers/sectios/informes/informes.module#InformesModule' },
            { path: 'perfil', loadChildren: './containers/sectios/usuarios/usuarios.module#UsuariosModule' },
        ]
    },
    { path: '**', component: P404Component }
];
