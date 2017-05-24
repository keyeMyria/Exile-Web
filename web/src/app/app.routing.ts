import { Routes } from '@angular/router';

import { DashboardComponent } from './containers/pages/dashboard/dashboard.component';
import { AuthComponent } from './containers/pages/auth/auth.component';

export const AppRoutes: Routes = [
    { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
    {
        path: '', component: AuthComponent, children: [
            { path: 'auth', loadChildren: './containers/pages/auth/auth.module#AuthModule' }
        ]
    },
    {
        path: '', component: DashboardComponent, children: [
            { path: 'usuarios', loadChildren: './containers/sectios/usuarios/usuarios.module#UsuariosModule' },
            { path: 'operacion', loadChildren: './containers/sectios/operacion/operacion.module#OperacionModule' },
            { path: 'novedades', loadChildren: './containers/sectios/novedades/novedades.module#NovedadesModule' },
            { path: 'informes', loadChildren: './containers/sectios/informes/informes.module#InfomesModule' },
            { path: 'perfil', loadChildren: './containers/sectios/usuarios/usuarios.module#UsuariosModule' },
        ]
    },
    { path: '**', redirectTo: 'dashboard', pathMatch: 'full' }
];
