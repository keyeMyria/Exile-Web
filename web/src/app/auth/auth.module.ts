import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { LockComponent } from './lock/lock.component';
import { RegistroComponent } from './registro/registro.component';
import { AuthRoutes } from './auth.route';
import { AuthComponent } from './auth.component';
import { SampleModule } from '../shared';

@NgModule({
    imports: [
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        SampleModule,
        RouterModule.forChild(AuthRoutes)
    ],
    declarations: [
        AuthComponent,
        LoginComponent,
        LockComponent,
        RegistroComponent
    ],
    providers: []
})
export class AuthModule { }
