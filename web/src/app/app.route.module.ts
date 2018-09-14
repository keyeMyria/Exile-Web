import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { AppRoutes } from './app.routing';
import { AuthGuard } from './shared';
import { AuthComponent } from './auth/auth.component';
// import { SelectiveStrategy } from './selective-strategy.service';
@NgModule({
    imports: [
        RouterModule.forRoot(AppRoutes, { useHash: true })
    ],
    exports: [RouterModule]
})
export class AppRouteModule { }
