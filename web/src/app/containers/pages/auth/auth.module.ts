import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { CallService } from '../../../call.service';
import { LoginComponent } from './login/login.component';
import { LockComponent } from './lock/lock.component';
import { RegistroComponent } from './registro/registro.component';
import { AuthService } from './auth.service';
import { AuthRoutes } from './auth.route';


@NgModule({
    imports: [
        FormsModule,
        ReactiveFormsModule,
        RouterModule.forChild(AuthRoutes)
    ],
    declarations: [
        LoginComponent,
        LockComponent,
        RegistroComponent
    ],
    providers: [
        AuthService
    ]
})
export class AuthModule { }
