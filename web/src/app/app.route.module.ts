import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { AppRoutes } from './app.routing';
import { AuthGuard } from './services/auth.guard';
import { LibModule } from './lib/lib.module';
import { AuthComponent } from './auth/auth.component';

@NgModule({
    imports: [
        BrowserModule,
        LibModule,
        RouterModule.forRoot(AppRoutes)
    ],
    declarations: [
        AuthComponent
    ],
    providers: [
        AuthGuard
    ],
    exports: [RouterModule]
})
export class AppRouteModule { }
