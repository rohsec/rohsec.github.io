if ('serviceWorker' in navigator) {
    // Unregister any existing service workers
    navigator.serviceWorker.getRegistrations().then(function(registrations) {
        for (let registration of registrations) {
            registration.unregister();
        }
    }).catch(function(error) {
        console.error("Error unregistering service workers:", error);
    });

    // Register minicoi.js service worker
    navigator.serviceWorker.register('/assets/scripts/minicoi.js', { scope: './' })
        .then(function(registration) {
            console.log('Service Worker minicoi.js registered with scope:', registration.scope);
        }).catch(function(error) {
            console.error('Service Worker registration failed:', error);
        });
}
