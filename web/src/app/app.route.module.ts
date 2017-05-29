import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { AppRoutes } from './app.routing';
import { AuthGuard } from './containers/pages/auth/auth.guard';
import { BaseComponent } from './containers/pages/base/base.component';
import { AuthComponent } from './containers/pages/auth/auth.component';
import { P404Component } from './containers/pages/404/404.component';
import { AuthService } from './containers/pages/auth/auth.service';

@NgModule({
    imports: [
        BrowserModule,
        RouterModule.forRoot(AppRoutes)
    ],
    providers: [
        AuthService,
        AuthGuard
    ],
    declarations: [
        BaseComponent,
        AuthComponent,
        P404Component
    ],
    exports: [RouterModule]
})
export class AppRouteModule { }
