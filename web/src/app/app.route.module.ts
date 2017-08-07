import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { AppRoutes } from './app.routing';
import { AuthGuard } from './auth/auth.guard';
import { AuthComponent } from './auth/auth.component';
import { SelectiveStrategy } from './selective-strategy.service';
@NgModule({
    imports: [
        RouterModule.forRoot(AppRoutes, { useHash: true, preloadingStrategy: SelectiveStrategy })
    ],
    providers: [SelectiveStrategy],
    exports: [RouterModule]
})
export class AppRouteModule { }
