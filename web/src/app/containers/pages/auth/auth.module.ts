import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

import { LoginComponent } from './login/login.component';
import { LockComponent } from './lock/lock.component';
import { RegistroComponent } from './registro/registro.component';

import { AuthRoutes } from './auth.route';

@NgModule({
    imports: [
        CommonModule,
        RouterModule.forChild(AuthRoutes)
    ],
    declarations: [
        LoginComponent,
        LockComponent,
        RegistroComponent
    ],
    providers: []
})
export class AuthModule { }
