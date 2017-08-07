import { Routes } from '@angular/router';

import { LoginComponent } from './login/login.component';
import { LockComponent } from './lock/lock.component';
import { RegistroComponent } from './registro/registro.component';
import { AuthComponent } from './auth.component';
export const AuthRoutes: Routes = [
    {
        path: '', component: AuthComponent, children: [
            { path: 'login', component: LoginComponent },
            { path: 'lock', component: LockComponent },
            { path: 'registro', component: RegistroComponent }
        ]
    }
];
