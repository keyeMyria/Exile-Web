import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';
import { CommonModule } from '@angular/common';
import { AppRouteModule } from './app.route.module';


import { AppComponent } from './app.component';
import { AuthService } from './services/auth.service';
import { CallService } from './services/call.service';
import { NotificationService } from './services/notification.service';

@NgModule({
    imports: [
        BrowserModule,
        HttpModule,
        CommonModule,
        AppRouteModule

    ],
    declarations: [
        AppComponent
    ],
    providers: [
        CallService,
        AuthService,
        NotificationService
    ],
    bootstrap: [AppComponent]
})

export class AppModule { }
