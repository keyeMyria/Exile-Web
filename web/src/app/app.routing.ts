import { Routes } from '@angular/router';
import { BaseComponent, P404Component, Menu } from 'componentex';
import { AuthGuard } from 'componentex';



export const AppRoutes: Routes = [
    { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
    {
        path: '', component: BaseComponent, canActivate: [AuthGuard], data: { preload: true }, children: [
            { path: '', loadChildren: './home/home.module#HomeModule' },
            { path: 'usuarios', loadChildren: './usuarios/usuarios.module#UsuariosModule' },
            { path: 'operacion', loadChildren: './operacion/operacion.module#OperacionModule' }
        ]
    },
    // { path: '**', component: P404Component }
];

import { UsuariosMenuMeta } from './usuarios/route';
import { OperacionMenuMeta } from './operacion/route';

Menu.instance.addMenu({ title: 'Inico', url: '/dashboard', icon: 'dashboard' });
Menu.instance.addMenu({ title: 'Usuarios', icon: 'supervisor_account', children: UsuariosMenuMeta })
Menu.instance.addMenu({ title: 'Operacion', icon: 'build', children: OperacionMenuMeta })
