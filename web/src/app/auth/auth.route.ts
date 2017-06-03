import { Routes } from '@angular/router';

import { LoginComponent } from './login/login.component';
import { LockComponent } from './lock/lock.component';
import { RegistroComponent } from './registro/registro.component';

export const AuthRoutes: Routes = [
    {
        path: '', children: [
            { path: 'login', component: LoginComponent },
            { path: 'lock', component: LockComponent },
            { path: 'registro', component: RegistroComponent }
        ]
    }
];
