import { Routes } from '@angular/router';

export const InformesRoutes: Routes = [
    {
        path: '', children: [
            { path: '', redirectTo: 'login', pathMatch: 'full' }
        ]
    }
];
