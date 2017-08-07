import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { LockComponent } from './lock/lock.component';
import { RegistroComponent } from './registro/registro.component';
import { AuthRoutes } from './auth.route';
import { AuthService } from './auth.service';
import { AuthGuard } from './auth.guard'
import { AuthComponent } from './auth.component';
@NgModule({
    imports: [
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        RouterModule.forChild(AuthRoutes)
    ],
    declarations: [
        AuthComponent,
        LoginComponent,
        LockComponent,
        RegistroComponent
    ],
    providers: [
        AuthService,
        AuthGuard
    ]
})
export class AuthModule { }
