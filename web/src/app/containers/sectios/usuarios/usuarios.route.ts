import { Routes } from '@angular/router';

import {  } from './';

export const UsuariosRoutes: Routes = [
    {
        path: '', children: [
            { path: '', redirectTo: 'login', pathMatch: 'full' }
        ]
    }
];
