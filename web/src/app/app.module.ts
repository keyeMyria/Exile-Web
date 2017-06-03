import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';
import { CommonModule } from '@angular/common';
import { AppRouteModule } from './app.route.module';


import { AppComponent } from './app.component';
import { AuthService } from './auth/auth.service';
import { CallService } from './call.service';


@NgModule({
    imports: [
        BrowserModule,
        HttpModule,
        CommonModule,
        AppRouteModule,

    ],
    declarations: [
        AppComponent
    ],
    providers: [
        CallService,
        AuthService
    ],
    bootstrap: [AppComponent]
})

export class AppModule { }
