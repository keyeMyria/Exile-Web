import { Routes } from '@angular/router';

export const NovedadesRoutes: Routes = [
    {
        path: '', children: [
            { path: '', redirectTo: 'login', pathMatch: 'full' }
        ]
    }
];
