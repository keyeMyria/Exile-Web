import { Routes } from '@angular/router';
import { BaseComponent, P404Component, Menu } from './shared';
import { AuthGuard } from './shared';



export const AppRoutes: Routes = [
    { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
    {
        path: '', component: BaseComponent, canActivate: [AuthGuard], data: { preload: true }, children: [
            { path: '', loadChildren: './home/home.module#HomeModule' },
            { path: 'usuarios', loadChildren: './usuarios/usuarios.module#UsuariosModule' },
            { path: 'operacion', loadChildren: './operacion/operacion.module#OperacionModule' },
            { path: 'novedades', loadChildren: './novedades/novedades.module#NovedadesModule' },
            { path: 'configuracion', loadChildren: './configuracion/configuracion.module#ConfiguracionModule' }
        ]
    },
    // { path: '**', component: P404Component }
];
